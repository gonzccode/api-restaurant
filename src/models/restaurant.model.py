from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
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


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    url = Column(String, nullable=False)
    restaurant_fk_id = Column(Integer, ForeignKey('restaurants.id'))

    restaurant_fk = relationship('Restaurant', back_populates='dishes')

