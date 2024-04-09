# do ORM_SQL.py

# ZADANIE

# 1 Tworzenie tabeli

# Bazy:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, String, Integer, Date, Numeric, ForeignKey

# фабрика сессий с првязкой к движку
Base = declarative_base()


# Class с колонкой, указывать имя класса какое хочется к колонке
class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    surname = Column(String(50))
    rating = Column(Integer)

    def __repr__(self):
        return self.name + " " + self.surname


class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    year = Column(Integer)
    category = Column(String(50))
    rating = Column(Integer)
    director_id = Column(Integer, ForeignKey("directors.id"))
    director = relationship("Director", backref="directors")


# Движок базы
db = create_engine(
    "mysql+mysqlconnector://root:!IloveOliwer1911@localhost:3306/cinematic", echo=True
)

# !!!!!!!!!!!!commit!!!!!!!!!!!!!!!!
Base.metadata.create_all(db)
