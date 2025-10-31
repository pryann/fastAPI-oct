from fastapi import Depends
from ...database import get_session
from .repository import AuthRepo
from .service import AuthService
from sqlalchemy.orm import Session


def get_auth_repo(db: Session = Depends(get_session)) -> AuthRepo:
    return AuthRepo(db)


def get_auth_service(repo: AuthRepo = Depends(get_auth_repo)) -> AuthService:
    return AuthService(repo)
