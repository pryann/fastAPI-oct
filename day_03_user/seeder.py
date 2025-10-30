from models import ProductModel
from database import Base, Session, engine


db = Session()

Base.metadata.create_all(bind=engine)

try:
    products = [
        ProductModel(name="Laptop", price=999.99),
        ProductModel(name="Monitor", price=88.9),
        ProductModel(name="VGA", price=1999.5),
        ProductModel(name="Keyboard", price=199.9),
        ProductModel(name="Mouse", price=9.9),
    ]
    db.add_all(products)
    db.commit()
    print(f"Inserted {len(products)} products into the database.")
except Exception as e:
    db.rollback()
    print(f"An error occurred: {e}")
finally:
    db.close()
