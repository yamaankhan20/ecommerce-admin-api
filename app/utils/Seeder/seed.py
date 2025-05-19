from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models import Products, Categories, Inventory, Sales
from datetime import datetime, timedelta
import random


def seed():
    db: Session = SessionLocal()
    try:
        #clear old data
        db.query(Sales).delete()
        db.query(Inventory).delete()
        db.query(Products).delete()
        db.query(Categories).delete()

        # create categories
        categories = [Categories(name=name) for name in ["Electronics", "Clothing", "Home"]]
        db.add_all(categories)
        db.flush()

        # create products
        products = []
        for i in range(10):
            product = Products(
                name=f"Product {i+1}",
                sku=f"SKU-{i+1:03}",
                price=round(random.uniform(10.0, 100.0), 2),
                category_id=random.choice(categories).id,
            )
            products.append(product)
        db.add_all(products)
        db.flush()

        # create inventory
        inventory = [
            Inventory(product_id=product.id, stock_level=random.randint(0, 20))
            for product in products
        ]
        db.add_all(inventory)

        # Create Sales over past 12 months
        now = datetime.now()
        sales = []
        for product in products:
            for months_ago in range(12):
                sale_date = now - timedelta(days=30 * months_ago)
                quantity = random.randint(1, 5)
                sale = Sales(
                    product_id=product.id,
                    quantity=quantity,
                    price=product.price,
                    sale_date=sale_date
                )
                sales.append(sale)
        db.add_all(sales)
        db.commit()
        print("Seed data inserted successfully.")

    except Exception as e:
        db.rollback()
        print("Error seeding data:", e)
    finally:
        db.close()


if __name__ == "__main__":
    seed()
