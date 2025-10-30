from day_02_products.models import Product
from day_03_sql.database import Session


db = Session()

try:
    products = [
        Product(name="Laptop", price=999.99),
        Product(name="Monitor", price=88.9),
        Product(name="VGA", price=1999.5),
        Product(name="Keyboard", price=199.9),
        Product(name="Mouse", price=9.9),
    ]
    db.add_all(products)
    db.commit()
    print(f"Inserted {len(products)} products into the database.")
except Exception as e:
    db.rollback()
    print(f"An error occurred: {e}")
finally:
    db.close()
