from typing import Annotated
from pydantic import BaseModel, Field, PositiveInt


class BaseItem(BaseModel):
    name: str
    quantity: Annotated[int, Field(gte=0)]


class Item(BaseItem):
    id: PositiveInt
