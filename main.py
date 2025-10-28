from fastapi import FastAPI, HTTPException

import uvicorn

from models import BaseItem, Item
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


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="localhost")
