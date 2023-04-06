import datetime
from sqlalchemy import Column, DateTime, Integer, Float, String, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from ..database.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    restaurants = relationship('Restaurant', back_populates='user_fk')


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_fk_id = Column(Integer, ForeignKey('users.id'))

    user_fk = relationship('User', back_populates='restaurants')
    dishes = relationship('Dish', back_populates='restaurant_fk')
    sold_restaurant_fk = relationship('DishesSold', back_populates='restaurant_sold')


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    url = Column(String, nullable=False)
    is_active_day = Column(Integer, nullable=False)
    restaurant_fk_id = Column(Integer, ForeignKey('restaurants.id'))

    restaurant_fk = relationship('Restaurant', back_populates='dishes')
    sold_dish_fk = relationship('DishesSold', back_populates='dish_sold')


class DishesSold(Base):
    __tablename__ = 'dishes_sold'
    # aqui la tabla tendria id, restaurant_fk_id, dish_fk_id, name, price_total, quantity, date,
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    total_price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    date_buy = Column(DateTime, default=datetime.datetime.utcnow())
    restaurant_fk_id = Column(Integer, ForeignKey('restaurants.id'))
    dish_fk_id = Column(Integer, ForeignKey('dishes.id'))

    restaurant_sold = relationship('Restaurant', back_populates='sold_restaurant_fk')
    dish_sold = relationship('Dish', back_populates='sold_dish_fk')
