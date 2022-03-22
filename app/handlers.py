import uuid
from datetime import datetime

from starlette import status
from fastapi import APIRouter, Body, Depends, HTTPException
from app.forms import UserLoginForm, UserCreateForm
from app.models import conn_db, User, AuthToken
from app.utils import get_password_hash

router = APIRouter()


@router.post('/login', name='user:login')
def login(user_form: UserLoginForm = Body(..., embed=True), database=Depends(conn_db)):
    user = database.query(User).filter(User.email == user_form.email).one_or_none()
    if not user or get_password_hash(user_form.password) != user.password:
        return {'error': 'email/password invalid'}

    token = AuthToken(token=str(uuid.uuid4()), user_id=user.id)
    database.add(token)
    database.commit()

    return {'status': 'OK'}


@router.post('/user', name='user:create')
def create_user(user: UserCreateForm = Body(..., embed=True), database=Depends(conn_db)):
    exist_user = database.query(User.id).filter(User.email == user.email).one_or_none()
    if exist_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='email already exists')
    new_user = User(
        email=user.email,
        password=get_password_hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        login=user.login
    )
    database.add(new_user)
    database.commit()
    return {'user_id': new_user.id}
