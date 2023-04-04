from ..database.db import SessionLocal, engine, Base
from ..models.restaurant_model import User, Restaurant, Dish
from ..utils.encrypt import create_hashed_password, validate_password
from sqlalchemy import text


Base.metadata.create_all(bind=engine)


def create_user(username, password):
    db = SessionLocal()
    new_password = create_hashed_password(password)
    print("new_password => ", new_password)
    user = User(username=username, password=new_password)
    db.add(user)
    db.commit()
    print("usuario creado")


def login(usermane, password):
    with engine.connect() as connection:
        result = connection.execute(text(f"select id, username, password from users where username = '{usermane}';"))
        password_db = None

        for row in result:
            password_db = row.password

        connection.close()

        login_value = validate_password(password, password_db)

        if login_value:
            print("ingreso exitoso")
        else:
            print("credenciales incorrectas")



