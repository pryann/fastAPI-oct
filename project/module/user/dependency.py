# optional, can be used for user-related dependencies in the module

from fastapi import Depends
from sqlalchemy.orm import Session
from ...database import get_session
from .service import UserService
from .repository import UserRepo


def get_user_repo(db: Session = Depends(get_session)) -> UserRepo:
    return UserRepo(db)


def get_user_service(repo: UserRepo = Depends(get_user_repo)) -> UserService:
    return UserService(repo)
