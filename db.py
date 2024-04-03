import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine(
    "mysql+pymysql://root:root@localhost:3306/poll_app")
session = sessionmaker(bind=engine)
