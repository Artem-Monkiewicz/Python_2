from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()


class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    surname = Column(String(50))
    rating = Column(Integer)

    def __repr__(self):
        return self.name + " " + self.surname


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    category = Column(String(50))
    year = Column(Integer)
    rating = Column(Integer)
    director_id = Column(Integer, ForeignKey("directors.id"))
    director = relationship("Director", backref="directors")

    def __repr__(self):
        return self.title


db = create_engine(
    "mysql+mysqlconnector://root:!IloveOliwer1911@localhost:3306/cinematic", echo=True
)

Base.metadata.create_all(db)

# !Ciekawostka - jeżeli znaki specjalne w hasle
# from urllib.parse import quote_plus
# db = create_engine('mysql+mysqlconnector://root:%s@localhost:3306/cinematic' % quote_plus('aJSSBVkmtQQCdetovrmR'),
