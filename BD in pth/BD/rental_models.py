from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine(
    "mysql+mysqlconnector://xxx:xxx@localhost:3306/car_rentals", echo=True
)
Base = declarative_base()


class Cars(Base):
    __tablename__ = "cars"

    car_id = Column(Integer, primary_key=True, autoincrement=True)
    producer = Column(String(30), nullable=False)
    model = Column(String(30), nullable=False)
    year = Column(Integer, nullable=False)
    horse_power = Column(Integer, nullable=False)
    price_per_day = Column(Integer, nullable=False)
    bookings = relationship("Bookings", back_populates="cars", cascade="all, delete")

    def __repr__(self):
        return f"{self.producer} {self.model} {self.price_per_day}"


class Clients(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    bookings = relationship("Bookings", back_populates="clients", cascade="all, delete")

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Bookings(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.client_id"), nullable=False)
    car_id = Column(Integer, ForeignKey("cars.car_id"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_amount = Column(Integer, nullable=False)
    clients = relationship("Clients", back_populates="bookings")
    cars = relationship("Cars", back_populates="bookings")

    def __repr__(self):
        return f"{self.start_date} - {self.end_date} {self.total_amount}"


Base.metadata.create_all(engine)
