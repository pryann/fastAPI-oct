# optional, can be used for user-related repository functions in the module


from sqlalchemy import select
from sqlalchemy.orm import Session

from .model import UserModel


class UserRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_users(self):
        stmt = select(UserModel)
        return self.db.scalars(stmt).all()

    def find_user(self, user_id: int):
        stmt = select(UserModel).where(UserModel.id == user_id)
        return self.db.scalars(stmt).first()

    def update_user(self, user_id: int, user_payload):
        existing_user = self.find_user(user_id)

        for key, value in user_payload.model_dump().items():
            setattr(existing_user, key, value)

        self.db.commit()
        self.db.refresh(existing_user)

        return existing_user

    def remove_user(self, user_id: int):
        self.db.delete(self.find_user(user_id))
        self.db.commit()
