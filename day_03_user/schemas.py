from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    price: float


class Product(ProductBase):
    # new in pydantic v2
    model_config = ConfigDict(from_attributes=True)

    id: int


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
