from datetime import datetime
from typing import Annotated, Literal, Optional
from pydantic import BaseModel, Field, PositiveInt, PositiveFloat


# you can create a Base model for shared attributes if needed
class Product(BaseModel):
    id: PositiveInt
    name: str
    stock: Annotated[int, Field(ge=0)]
    color: Literal["red", "green", "blue", "yellow"]
    price: PositiveFloat
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None


class ProductCreate(BaseModel):
    name: str
    stock: Annotated[int, Field(ge=0)] = 0
    color: Literal["red", "green", "blue", "yellow"]
    price: PositiveFloat


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    stock: Optional[Annotated[int, Field(ge=0)]] = None
    color: Optional[Literal["red", "green", "blue", "yellow"]] = None
    price: Optional[PositiveFloat] = None


class ProductQuery(BaseModel):
    color: Optional[Literal["red", "green", "blue", "yellow"]] = None
    stock: Optional[int] = None
    offset: Annotated[int, Field(ge=0)] = 0
    limit: Annotated[int, Field(ge=1, le=100)] = 10
