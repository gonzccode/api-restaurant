from datetime import datetime
from ..database.db import Base, engine, SessionLocal
from ..models.restaurant_model import Restaurant, Dish, DishesSold


Base.metadata.create_all(bind=engine)


def get_all_restaurants():
    db = SessionLocal()
    restaurants = db.query(Restaurant).all()
    restaurants_list = [{"id": rest.id, "name": rest.name} for rest in restaurants]
    return restaurants_list


def get_diner_restaurant_id(rid):
    db = SessionLocal()
    restaurant = db.query(Restaurant).filter(Restaurant.id == rid).one()
    return restaurant


def get_diner_restaurant_dishes(rid):
    db = SessionLocal()
    today = datetime.today()
    number_today = int(today.weekday()+1)
    dishes = db.query(Dish).filter(Dish.restaurant_fk_id == rid, Dish.is_active_day == number_today).all()
    dishes_list = [{"id": dish.id, "name": dish.name, "price": dish.price} for dish in dishes]
    return dishes_list


def get_diner_restaurant_dish(rid, did):
    db = SessionLocal()
    dish = db.query(Dish).filter(Dish.id == did, Dish.restaurant_fk_id == rid).one()
    return dish


def post_diner_dish_buy(name, total_price, quantity, restaurant_fk_id, dish_fk_id):
    db = SessionLocal()
    dish_buy = DishesSold(name=name, total_price=total_price, quantity=quantity,
                          restaurant_fk_id=restaurant_fk_id, dish_fk_id=dish_fk_id)
    db.add(dish_buy)
    db.commit()
