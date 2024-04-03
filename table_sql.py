from flask import session
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey, String, Integer, Float, Column, Text

Base = declarative_base()


class MyGoods(Base):
    __tablename__ = "my_goods"
    Good_name = Column(String(50))
    Price = Column(Float)
    Amount = Column(Integer)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100))
    Age = Column(Integer)


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, nullable=False, primary_key=True)
    Description = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))


connection = session()
res = connection.execute(sqlalchemy.text("SELECT * from Users"))
print(res.fetchall())

new_good = MyGoods()
new_good.Good_name = "Apple"
new_good.Price = 12.5
new_good.Amount = 1
connection.add(new_good)
connection.commit()
