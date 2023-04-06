from sqlalchemy import text
from ..database.db import Base, engine, SessionLocal
from ..models.restaurant_model import Restaurant, Dish, DishesSold


Base.metadata.create_all(bind=engine)


def get_all_restaurants():
    db = SessionLocal()
    restaurants = db.query(Restaurant).all()
    for rest in restaurants:
        print("restaurant => ", rest.id, rest.name)
    return restaurants



