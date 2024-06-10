from sqlalchemy import create_engine, select, and_, func
from sqlalchemy.orm import sessionmaker
from rental_models import Cars, Clients, Bookings

engine = create_engine(
    "mysql+mysqlconnector://xxx:xxx@localhost:3306/car_rentals", echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

# car1 = session.query(Cars).get(1)
# print(car1.bookings)

# Wypisz wszystkie rezerwacje dla klienta o id = 3. Spróbuj zarówno za pomocą query() jak i funkcji select().
# #1
# client3 = session.query(Clients).get(3)
# print(client3.bookings)
# #2
# client4 = session.query(Bookings).filter_by(client_id=3).all()
# print(client4)
# #3
# client5 = session.query(Bookings).filter(Bookings.client_id == 3).all()
# print(client3.bookings)
# #4
# conn = db.connect()

# bookings = conn.execute(select(Bookings).where(Bookings.client_id == 3)).fetchall()

# print(bookings)
# #5
# cars = session.query(Bookings, Cars).join(Cars).filter(Bookings.client_id == 5).all()

# for car in cars:
#     print(car)

# ZADANIE

# Wypisz sumę kosztów wszystkich rezerwacji dla każdego klienta, imię oraz nazwisko klienta dla rezerwacji, które zostały zrealizowane w okresie 10-17.07.2020.

# conn = db.connect()
# zm = func.sum(Bookings.total_amount)
# results = session.query(Clients.name, Clients.surname, zm)
# results = results.join(Bookings)
# results = results.filter(and_(Bookings.start_date >= '2020-07-10', Bookings.end_date <= '2020-07-17'))
# results = results.group_by(Clients.client_id)
# results = results.all()

# print(results)
