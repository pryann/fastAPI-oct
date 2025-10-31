from .const import JWT_SECRET
from .schema import Login, Registration
from .repository import AuthRepo
import bcrypt
import jwt


class AuthService:
    def __init__(self, repo: AuthRepo):
        self.repo = repo

    def __hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        password_bytes = password.encode("utf-8")
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed.decode("utf-8")

    def __verify_password(self, plain_password: str, hashed_password: str) -> bool:
        plain_password_bytes = plain_password.encode("utf-8")
        hashed_password_bytes = hashed_password.encode("utf-8")
        return bcrypt.checkpw(plain_password_bytes, hashed_password_bytes)

    def __generate_access_token(self, user_id: int) -> str:
        payload = {"user_id": user_id}
        return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

    def registration(self, registration_payload: Registration):
        existed_user = self.repo.find_user_by_email(registration_payload.email)

        if existed_user:
            # you can create a custom exception for this case
            raise ValueError("User with this email already exists")

        registration_payload.password = self.__hash_password(
            registration_payload.password
        )

        self.repo.registration(registration_payload)

    def login(self, login_payload: Login):
        existed_user = self.repo.find_user_by_email(login_payload.email)

        if not existed_user:
            # you can create a custom exception for this case
            raise ValueError("Invalid email")

        is_password_valid = self.__verify_password(
            login_payload.password, existed_user.password
        )

        if not is_password_valid:
            # you can create a custom exception for this case
            raise ValueError("Invalid email or password")

        return self.__generate_access_token(existed_user.id)

    def me(self, user_id: int):
        user = self.repo.me(user_id)

        if not user:
            raise ValueError("User not found")

        return user
