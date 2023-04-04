from ..database.db import SessionLocal, engine, Base
from ..models.restaurant_model import User, Restaurant, Dish
from sqlalchemy import text


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
        password_db = None

        for row in result:
            password_db = row.password

        connection.close()
        return password_db


def logout_user():
    pass


def register_restaurant():
    pass

def add_dish():
    pass


def update_dish():
    pass


def delete_dish():
    pass


#listar los platos del dia
def get_dishes():
    pass


#platos vendidos (cantidad de platos, cuanto dinero gano)
def get_dishes_sold():
    pass



