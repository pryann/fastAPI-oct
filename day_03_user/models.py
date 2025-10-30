from sqlalchemy import Float, Integer, String
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

# user
# - id
# - email
# - first_name
# - last_name
# - email
# - pass
# - terms_accepted: bool
# - newsletter: bool
# - created_at: bool
# - updated_at: bool
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


class ProductModel(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Float(), nullable=False)
