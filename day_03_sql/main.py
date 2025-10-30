from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from database import get_session
from models import ProductModel
from schemas import Product
from sqlalchemy.orm import Session

app = FastAPI()

# use query API


@app.get("/products", response_model=list[Product])
async def get_products(db: Session = Depends(get_session)):
    products = db.query(ProductModel).all()
    return products


@app.get("/products/{product_id}", response_model=Product)
async def find_product_by_id(product_id: int, db: Session = Depends(get_session)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")
