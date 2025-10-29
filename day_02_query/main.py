from typing import Annotated
from fastapi import FastAPI, Query

import uvicorn
from database import items
from models import Item, QueryParams

app = FastAPI()


@app.get("/items", response_model=list[Item])
async def get_items(query: Annotated[QueryParams, Query()]):
    # items[0:3]
    sorted_items = sorted(
        items,
        key=lambda item: getattr(item, query.order_by),
        reverse=bool(query.reverse),
    )
    return sorted_items[query.offset : query.offset + query.limit]


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="localhost")
