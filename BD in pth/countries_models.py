from sqlalchemy import (
    create_engine,
    Column,
    String,
    Integer,
    Date,
    text,
    ForeignKey,
    Float,
)
from sqlalchemy.orm import declarative_base, sessionmaker


# create DB countries
engine = create_engine(
    "mysql+mysqlconnector://root:!IloveOliwer1911@localhost:3306", echo=True
)

Session = sessionmaker(bind=engine)
session = Session()
session.execute(text("CREATE DATABASE IF NOT EXISTS countries;"))
session.commit()

engine = create_engine(
    "mysql+mysqlconnector://root:!IloveOliwer1911@localhost:3306/countries", echo=True
)
Base = declarative_base()


class Countries(Base):
    __tablename__ = "countries"

    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(128))
    region = Column(String(128))
    population = Column(Integer)
    area = Column(Integer)
    population_density = Column(Float)
    coastline = Column(Float)
    net_migration = Column(Float)
    infant_mortality = Column(Float)
    gdp_per_capita = Column(Float)
    literacy = Column(Float)
    phones = Column(Float)
    arable = Column(Float)
    crops = Column(Float)
    other = Column(Float)
    climate = Column(Float)
    birthrate = Column(Float)
    deathrate = Column(Float)
    agriculture = Column(Float)
    industry = Column(Float)
    service = Column(Float)

    def __repr__(self):
        return self.country


Base.metadata.create_all(engine)
