from fastapi import FastAPI, HTTPException

import uvicorn

from models import Item
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


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="localhost")
