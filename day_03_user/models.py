from datetime import datetime
from pydantic import EmailStr
from sqlalchemy import Boolean, DateTime, Float, Integer, String, func
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

# user
# - id
# - first_name
# - last_name
# - email
# - pass
# - terms_accepted: bool
# - newsletter: bool
# - created_at: datetime
# - updated_at: datetime

#   created_at: Mapped[DateTime] = mapped_column(
#         DateTime, default=func.current_timestamp(), nullable=False
#     )
#     updated_at: Mapped[DateTime] = mapped_column(
#         DateTime,
#         default=func.current_timestamp(),
#         onupdate=func.current_timestamp(),
#         nullable=False,
#     )
# PATCH: first_name, last_name, newsletter


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, index=True)
    email: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False, index=True
    )
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    terms_accepted: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    newsletter: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=False,
    )
