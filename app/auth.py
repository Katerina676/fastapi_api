from fastapi import Depends, HTTPException
from starlette import status

from app.models import AuthToken, conn_db


def check_token(token: str, database=Depends(conn_db)):
    auth_token = database.query(AuthToken).filter(AuthToken.token == token).one_or_none()
    if auth_token:
        return auth_token

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Auth is failed',
    )
