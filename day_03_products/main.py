import datetime
from typing import Annotated
from fastapi import FastAPI, HTTPException, Query

import uvicorn

# absolute imports
# from day_03_products.models import Product, ProductCreate, ProductUpdate, ProductQuery
# from day_03_products.database import products, get_next_id
from .models import Product, ProductCreate, ProductUpdate, ProductQuery
from .database import products, get_next_id

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/products", response_model=list[Product])
async def get_products(query: Annotated[ProductQuery, Query()]):
    filtered_products = products.copy()
    if query.color is not None:
        filtered_products = [
            product for product in filtered_products if product.color == query.color
        ]
    if query.stock is not None:
        filtered_products = [
            product for product in filtered_products if product.stock >= query.stock
        ]
    return filtered_products[query.offset : query.offset + query.limit]


@app.get("/products/{product_id}", response_model=Product)
async def find_product_by_id(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", response_model=Product, status_code=201)
async def create_product(product: ProductCreate):
    new_product = Product(id=get_next_id(), **product.model_dump())
    products.append(new_product)
    return new_product


@app.patch("/products/{product_id}", response_model=Product)
async def partial_update_product(product_id: int, product: ProductUpdate):
    for index, existing_product in enumerate(products):
        if existing_product.id == product_id:
            update_data = product.model_dump()
            update_data["updated_at"] = datetime.now()
            products[index] = existing_product.model_copy(update=update_data)
            return products[index]
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}", status_code=204)
async def remove_product(product_id: int):
    for index, existing_product in enumerate(products):
        if existing_product.id == product_id:
            del products[index]


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="localhost")
