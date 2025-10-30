from models import UserModel
from database import Base, Session, engine


db = Session()

Base.metadata.create_all(bind=engine)

try:
    products = [
        UserModel(name="Laptop", price=999.99),
        UserModel(name="Monitor", price=88.9),
        UserModel(name="VGA", price=1999.5),
        UserModel(name="Keyboard", price=199.9),
        UserModel(name="Mouse", price=9.9),
    ]
    db.add_all(products)
    db.commit()
    print(f"Inserted {len(products)} products into the database.")
except Exception as e:
    db.rollback()
    print(f"An error occurred: {e}")
finally:
    db.close()
