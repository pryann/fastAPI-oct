from sqlalchemy import Float, Integer, String
from database import Base
from sqlalchemy.orm import Mapped, mapped_column


class ProductModel(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Float(), nullable=False)
