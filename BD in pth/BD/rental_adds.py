from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from rental_models import Cars, Clients, Bookings

engine = create_engine(
    "mysql+mysqlconnector://xxx:xxx@localhost:3306/car_rentals", echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

# client_1 = Clients(
#     name="Jan", surname="Nowak", adress="ul. Florianska 12", city="Krakow"
# )
# car_1 = Cars(
#     producer="Seat", model="Leon", year=2016, horse_power=80, price_per_day=200
# )

# session.add(client_1)
# session.add(car_1)
# session.commit()

# Edit surname
# client_1 = session.query(Clients).get(1)
# client_1.surname = "Kowalski"
# session.commit()

# delete
# session.query(Clients).filter(Clients.client_id == 1).delete(synchronize_session=False)
# session.commit()

# show
# result = session.query(Cars).all()
# print(result)

# result2 = session.query(Clients).all()
# print(result2)

clients = [
    {
        "name": "Jan",
        "surname": "Kowalski",
        "address": "ul. Florianska 12",
        "city": "Krakow",
    },
    {
        "name": "Andrzej",
        "surname": "Nowak",
        "address": "ul. Saska 43",
        "city": "Wroclaw",
    },
    {
        "name": "Michal",
        "surname": "Taki",
        "address": "os. Srodkowe 12",
        "city": "Poznan",
    },
    {"name": "Pawel", "surname": "Ktory", "address": "ul. Stara 11", "city": "Gdynia"},
    {"name": "Anna", "surname": "Inna", "address": "os. Srednie 1", "city": "Gniezno"},
    {"name": "Alicja", "surname": "Panna", "address": "os. Duze 33", "city": "Torun"},
    {
        "name": "Damian",
        "surname": "Papa",
        "address": "ul. Skosna 66",
        "city": "Warszawa",
    },
    {"name": "Marek", "surname": "Troska", "address": "os. Male 90", "city": "Radom"},
    {
        "name": "Jakub",
        "surname": "Klos",
        "address": "os. Polskie 19",
        "city": "Wadowice",
    },
    {
        "name": "Lukasz",
        "surname": "Lis",
        "address": "os. Podlaskie 90",
        "city": "Bialystok",
    },
]
cars = [
    {
        "producer": "Seat",
        "model": "Leon",
        "year": 2016,
        "horse_power": 80,
        "price_per_day": 200,
    },
    {
        "producer": "Toyota",
        "model": "Avensis",
        "year": 2014,
        "horse_power": 72,
        "price_per_day": 100,
    },
    {
        "producer": "Mercedes",
        "model": "CLK",
        "year": 2018,
        "horse_power": 190,
        "price_per_day": 400,
    },
    {
        "producer": "Hyundai",
        "model": "Coupe",
        "year": 2014,
        "horse_power": 165,
        "price_per_day": 300,
    },
    {
        "producer": "Dacia",
        "model": "Logan",
        "year": 2015,
        "horse_power": 103,
        "price_per_day": 150,
    },
    {
        "producer": "Saab",
        "model": "95",
        "year": 2012,
        "horse_power": 140,
        "price_per_day": 140,
    },
    {
        "producer": "BMW",
        "model": "E36",
        "year": 2007,
        "horse_power": 110,
        "price_per_day": 80,
    },
    {
        "producer": "Fiat",
        "model": "Panda",
        "year": 2016,
        "horse_power": 77,
        "price_per_day": 190,
    },
    {
        "producer": "Honda",
        "model": "Civic",
        "year": 2019,
        "horse_power": 130,
        "price_per_day": 360,
    },
    {
        "producer": "Volvo",
        "model": "XC70",
        "year": 2013,
        "horse_power": 180,
        "price_per_day": 280,
    },
]
bookings = [
    {
        "client_id": 3,
        "car_id": 3,
        "start_date": "2020-07-06",
        "end_date": "2020-07-08",
        "total_amount": 400,
    },
    {
        "client_id": 6,
        "car_id": 10,
        "start_date": "2020-07-10",
        "end_date": "2020-07-16",
        "total_amount": 1680,
    },
    {
        "client_id": 4,
        "car_id": 5,
        "start_date": "2020-07-11",
        "end_date": "2020-07-14",
        "total_amount": 450,
    },
    {
        "client_id": 5,
        "car_id": 4,
        "start_date": "2020-07-11",
        "end_date": "2020-07-13",
        "total_amount": 600,
    },
    {
        "client_id": 7,
        "car_id": 3,
        "start_date": "2020-07-12",
        "end_date": "2020-07-14",
        "total_amount": 800,
    },
    {
        "client_id": 5,
        "car_id": 7,
        "start_date": "2020-07-14",
        "end_date": "2020-07-17",
        "total_amount": 240,
    },
    {
        "client_id": 3,
        "car_id": 8,
        "start_date": "2020-07-14",
        "end_date": "2020-07-16",
        "total_amount": 380,
    },
    {
        "client_id": 5,
        "car_id": 9,
        "start_date": "2020-07-15",
        "end_date": "2020-07-18",
        "total_amount": 1080,
    },
    {
        "client_id": 6,
        "car_id": 10,
        "start_date": "2020-07-16",
        "end_date": "2020-07-20",
        "total_amount": 1120,
    },
    {
        "client_id": 8,
        "car_id": 1,
        "start_date": "2020-07-16",
        "end_date": "2020-07-19",
        "total_amount": 600,
    },
    {
        "client_id": 9,
        "car_id": 2,
        "start_date": "2020-07-16",
        "end_date": "2020-07-21",
        "total_amount": 500,
    },
    {
        "client_id": 10,
        "car_id": 6,
        "start_date": "2020-07-17",
        "end_date": "2020-07-19",
        "total_amount": 280,
    },
    {
        "client_id": 1,
        "car_id": 9,
        "start_date": "2020-07-17",
        "end_date": "2020-07-19",
        "total_amount": 720,
    },
    {
        "client_id": 3,
        "car_id": 7,
        "start_date": "2020-07-18",
        "end_date": "2020-07-21",
        "total_amount": 240,
    },
    {
        "client_id": 5,
        "car_id": 4,
        "start_date": "2020-07-18",
        "end_date": "2020-07-22",
        "total_amount": 1200,
    },
]


def insert_data(session, base, params):
    for param in params:
        session.add(base(**param))
        session.commit()


insert_data(session, Clients, clients)
insert_data(session, Cars, cars)
insert_data(session, Bookings, bookings)
