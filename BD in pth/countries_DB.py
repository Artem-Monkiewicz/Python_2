# query

from sqlalchemy import create_engine, select, and_, func
from sqlalchemy.orm import sessionmaker
from rental_models import Cars, Clients, Bookings

engine = create_engine(
    "mysql+mysqlconnector://xxx:xxx@localhost:3306/car_rentals", echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

# models
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine(
    "mysql+mysqlconnector://xxx:xxx@localhost:3306/car_rentals", echo=True
)
Base = declarative_base()

# adds

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from rental_models import Cars, Clients, Bookings

engine = create_engine(
    "mysql+mysqlconnector://root:!IloveOliwer1911@localhost:3306/car_rentals", echo=True
)

Session = sessionmaker(bind=engine)
session = Session()
