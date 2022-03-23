from datetime import datetime
from enum import Enum
from sqlalchemy import create_engine, String, Integer, Column, ForeignKey
from sqlalchemy.orm import Session
from app.config import DATABASE_URL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StreamStatus(Enum):
    PLANED = 'planed'
    ACTIVE = 'active'
    CLOSED = 'closed'


def conn_db():
    engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
    session = Session(bind=engine.connect())
    return session


class User(Base):
    __tablename__ = 'users'

    id =  Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    login = Column(String)
    created_at = Column(String, default=datetime.utcnow())

    def __str__(self):
        return f'[{self.id}]{self.email}'

    def get_filtered_data(self):
        return {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'login': self.login,
            'created_at': self.created_at
        }


class Stream(Base):
    __tablename__ = 'stream'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    topic = Column(String)
    status = Column(String, default=StreamStatus.PLANED.value)
    created_at = Column(String, default=datetime.utcnow())

    def __str__(self):
        return f'{self.id} - {self.title}[{self.topic}]'


class AuthToken(Base):
    __tablename__ = 'auth_token'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    token = Column(String)
    created_at = Column(String, default=datetime.utcnow())