from typing import Annotated, Literal
from pydantic import BaseModel, Field, PositiveInt


class Item(BaseModel):
    id: PositiveInt
    name: str
    quantity: Annotated[int, Field(gte=0)]


# offset: int = (0,)
# limit: int = (3,)
# order_by: Literal["id", "quantity"] = ("id",)
# reverse: int = (0,)


class QueryParams(BaseModel):
    offset: int = 0
    limit: int = 3
    order_by: Literal["id", "quantity"] = "id"
    reverse: Annotated[int, Field(ge=0, le=1)] = 0
