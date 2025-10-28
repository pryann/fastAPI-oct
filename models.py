from typing import Annotated
from pydantic import BaseModel, Field, PositiveInt


class Item(BaseModel):
    id: PositiveInt
    name: str
    quantity: Annotated[int, Field(gte=0)]
