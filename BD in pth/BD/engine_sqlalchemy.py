from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("mysql+mysqlconnector://xxx:xxx@localhost:3306/cinematic", echo=True)

Base = declarative_base()
Session = sessionmaker(bind=db)
session = Session()

print("session")
