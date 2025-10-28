import re
import stat
from fastapi import FastAPI, HTTPException

import uvicorn

from models import BaseItem, Item, PartialUpdateItem
from database import items

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/items", response_model=list[Item])
async def get_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
async def find_item_by_id(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, status_code=201)
# HTTP request body: { name: "Item 4" , quantity: 7}
async def create_item(item: BaseItem):
    max_id = max((item.id for item in items), default=0)
    # Item(id=max_id+1, name="Item 4",  quantity=7)
    # incoming JSON -> Pydantic model(Item) -> dictionary (model_dump()) -> unpacking (**) -> Item(...)

    # Incoming JOSN: { name: "Item 4" , quantity: 7} - simply str
    # Incoming JSON -> Pydantic model(BaseItem)
    # Pydantic model(BaseItem) -> dictionary (model_dump())
    # Unpacking (**) -> Item(...)
    new_item = Item(id=max_id + 1, **item.model_dump())
    items.append(new_item)
    return new_item


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: BaseItem):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            # in real life, you need to oerwrite the resource
            # The DB table and the entity is not equal to the Pydantic model
            items[index] = Item(id=item_id, **item.model_dump())
            return items[index]
    raise HTTPException(status_code=404, detail="Item not found")


@app.patch("/items/{item_id}", response_model=Item)
async def partial_update_item(item_id: int, item: PartialUpdateItem):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items[index] = existing_item.model_copy(
                update=item.model_dump(exclude_unset=True)
            )
            return items[index]
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
async def remove_item(item_id: int):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            del items[index]


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="localhost")
