from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from database import get_session
from models import ProductModel
from schemas import Product, ProductBase, ProductUpdate
from sqlalchemy.orm import Session

app = FastAPI()

# use query API

# @app.get("/products", response_model=list[Product])
# async def get_products(db: Session = Depends(get_session)):
#     products = db.query(ProductModel).all()
#     return products


# @app.get("/products/{product_id}", response_model=Product)
# async def find_product_by_id(product_id: int, db: Session = Depends(get_session)):
#     product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
#     if product:
#         return product
#     raise HTTPException(status_code=404, detail="Product not found")

# use select API


@app.get("/products", response_model=list[Product])
async def get_products(db: Session = Depends(get_session)):
    # query using select statement
    stmt = select(ProductModel)
    # use db session to execute the statement
    products = db.scalars(stmt).all()
    return products
    # return db.scalars(select(ProductModel)).all()


@app.get("/products/{product_id}", response_model=Product)
async def find_product_by_id(product_id: int, db: Session = Depends(get_session)):
    stmt = select(ProductModel).where(ProductModel.id == product_id)
    product = db.scalars(stmt).first()
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", response_model=Product, status_code=201)
async def create_product(product: ProductBase, db: Session = Depends(get_session)):
    new_product = ProductModel(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.patch("/products/{product_id}", response_model=Product)
async def update_product(
    product_id: int, product: ProductUpdate, db: Session = Depends(get_session)
):
    # find the product first
    stmt = select(ProductModel).where(ProductModel.id == product_id)
    existing_product = db.scalars(stmt).first()

    if existing_product:
        for key, value in product.model_dump(exclude_unset=True).items():
            setattr(existing_product, key, value)
        # existing_product.__dict__.update(product.model_dump(exclude_unset=True))
        db.commit()
        db.refresh(existing_product)
        return existing_product

    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}", status_code=204)
async def remove_product(product_id: int, db: Session = Depends(get_session)):
    stmt = select(ProductModel).where(ProductModel.id == product_id)
    existing_product = db.scalars(stmt).first()

    if existing_product:
        db.delete(existing_product)
        db.commit()
        return

    raise HTTPException(status_code=404, detail="Product not found")
