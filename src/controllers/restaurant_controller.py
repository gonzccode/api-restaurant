from ..database.db import SessionLocal, engine, Base
from ..models.restaurant_model import User, Restaurant, Dish, DishesSold
from sqlalchemy import text, update, delete, Table, and_


Base.metadata.create_all(bind=engine)


def register_user(username, password):
    db = SessionLocal()
    user = User(username=username, password=password)
    db.add(user)
    db.commit()
    print("created user")


def login_user(usermane):
    with engine.connect() as connection:
        result = connection.execute(text(f"select id, username, password from users where username = '{usermane}';"))
        id_user_db = None
        password_db = None

        for row in result:
            id_user_db = row.id
            password_db = row.password

        connection.close()
        return id_user_db, password_db


def logout_user():
    pass


def register_restaurant(name, user_id):
    db = SessionLocal()
    user = user_id
    #user = get_id_user(user_id)
    restaurant = Restaurant(name=name, user_fk_id=user)
    db.add(restaurant)
    db.commit()
    print("created restaurant")


def get_id_restaurant(name):
    with engine.connect() as connection:
        result = connection.execute(text(f"select id, name from restaurants where name = '{name}';"))
        id_restaurant = None

        for row in result:
            id_restaurant = row.id

        connection.close()
        return id_restaurant


def add_dish(name, price, url, status, id_restaurant):
    db = SessionLocal()
    #estatus será introduciendo el día miercoles, jueves etc, utilizar datetime
    dish = Dish(name=name, price=price, url=url, is_active_day=status, restaurant_fk_id=id_restaurant)
    db.add(dish)
    db.commit()
    print(f"created dish in restaurant {id_restaurant}")


def update_dish(name, price, url, status, rid, did):
    db = SessionLocal()
    new_dish = db.query(Dish).filter_by(id=did).one()
    new_dish.name = name
    new_dish.price = price
    new_dish.url = url
    new_dish.is_active_day = status
    db.merge(new_dish)
    db.commit()


def delete_dish(rid, did):
    db = SessionLocal()
    db.query(Dish).filter(Dish.id == did, Dish.restaurant_fk_id == rid).delete()
    db.commit()


def get_dish(rid, did):
    db = SessionLocal()
    dish = db.query(Dish).filter(Dish.id == did, Dish.restaurant_fk_id == rid).one()
    print("get dish => ", dish.id, dish.name, dish.price, dish.is_active_day)


#listar los platos del dia
def get_dishes(rid, day):
    db = SessionLocal()
    if not day:
        dishes = db.query(Dish).filter(Dish.restaurant_fk_id == rid).all()
        for dish in dishes:
            print("dish not day", dish.id, dish.name, dish.price)
    else:
        dishes = db.query(Dish).filter(Dish.restaurant_fk_id == rid, Dish.is_active_day == int(day)).all()
        for dish in dishes:
            print("dish yes day", dish.id, dish.name, dish.price)


#platos vendidos (cantidad de platos, cuanto dinero gano)
def get_dishes_sold(rid):
    db = SessionLocal()
    dishes_buy = db.query(DishesSold).filter(DishesSold.restaurant_fk_id == rid).all()
    for dish in dishes_buy:
        print("dish sold => ", dish.name, dish.total_price, dish.quantity, dish.date_buy)
    return dishes_buy
    #aqui la tabla tendria id, restaurant_fk_id, dish_fk_id, name, price_total, quantity, date,



