from sqlalchemy import select
from sqlalchemy.orm import Session

from .schema import Registration
from ..user.model import UserModel


class AuthRepo:
    def __init__(self, db: Session):
        self.db = db

    def find_user_by_email(self, email: str):
        stmt = select(UserModel).where(UserModel.email == email)
        return self.db.scalars(stmt).first()

    def registration(self, registration_payload: Registration):
        new_user = UserModel(**registration_payload.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def me(self, user_id: int):
        stmt = select(UserModel).where(UserModel.id == user_id)
        return self.db.scalars(stmt).first()
