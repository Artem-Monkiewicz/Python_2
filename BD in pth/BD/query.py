from sqlalchemy import create_engine, func, and_, or_, text, bindparam, Integer
from sqlalchemy.orm import sessionmaker, registry
from models2 import Director, Movie


db = create_engine("mysql+mysqlconnector://xxx:xxx@localhost:3306/cinematic", echo=True)

Session = sessionmaker(bind=db)
session = Session()

# result = session.query(Movie).filter_by(category='Drama').all()

# result = session.query(Movie).filter(and_(Movie.category == 'Crime', Movie.year > 1994)).all()

# result = session.query(Movie.title, Movie.category, Movie.rating)\
# .filter(and_(Movie.year >= 2000, Movie.year <= 2010, Movie.rating > 7))\
# .order_by(Movie.rating.desc()).all()

# result = session.query(Person).filter(Person.first_name.like('Pa%')).all()

# result = session.query(Person).filter(Person.first_name.in_(['Witold', 'Patryk'])).all()

# result = session.query(Person).filter(Person.first_name.in_(['Witold', 'Patryk'])).count()

# result = session.query(Director).filter(Director.rating >= 6, or_(Director.name.like('D%'), Director.name.like('%n'))).all()

# Wypisz imiona oraz nazwiska wszystkich reżyserów, których filmy zostały utworzone w latach  2011-2014, a ocena ich filmów jest mniejsza niż 9.

# result = (
#     session.query(Director.name, Director.surname)
#     .join(Movie)
#     .filter(and_(Movie.year >= 2011, Movie.year <= 2014), Movie.rating < 9)
#     .distinct()
#     .all()
# )

# Wypisz całkowitą liczbę stworzonych filmów dla każdego reżysera, jego imię i nazwisko, oraz średnią ocen każdego reżysera policzoną na podstawie ocen ich filmów.

# result = session.query(Director.name, Director.surname, func.count(Movie.id), func.avg(Movie.rating)).join(Movie).group_by(Movie.director_id).all()

# Otrzymane z poprzedniego zadania zapytanie, sformatuj do postaci tekstowej używając text().
# Zmodyfikuj je tak, aby można było użyć tego zapytania podając przedział lat, w których reżyserowie
# tworzyli filmy jako parametr do zapytania.

# q = text(
#     """
# SELECT directors.name AS directors_name, directors.surname AS directors_surname, count(movies.id) AS count_1, avg(movies.rating) AS avg_1
# FROM directors INNER JOIN movies ON directors.id = movies.director_id
# WHERE movies.year >= :start_year AND movies.year <= :stop_year
# GROUP BY movies.director_id
# """
# )
# q.bindparams(
#     bindparam('start_year', type_=Integer),
#     bindparam('stop_year', type_=Integer)
# )

# result = session.query(text('directors_name'), text('directors_surname'), text('count_1'), text('avg_1'))\
#     .from_statement(q).params(start_year=2000, stop_year=2010).all()

# ZADANIE
# Wypisz całkowitą liczbę stworzonych filmów dla każdego reżysera, jego imię i nazwisko, oraz średnią ocen każdego reżysera obliczoną na podstawie ocen ich filmów.

# ZADANIE 2

# Wszystkim reżyserom, których filmy zostały wyprodukowane przed rokiem 2001 oraz ich tytuł zaczyna się na literę 'T', zwiększ oceny o 1.
# 	Skorzystaj z transakcji.

# with session.begin():
#     results = session.query(Director).join(Movie).filter(and_(Movie.year < 2001, Movie.title.like('T%')))
#     for r in results:
#         r.rating += 1

# with session.begin():
#     movies = session.query(Movie.id).join(Director).filter(Director.name == 'Frank').all()
#     ids = [movie.id for movie in movies]
#     session.query(Movie).filter(Movie.id.in_(ids)).delete(synchronize_session=False)
#     session.query(Director).filter(Director.name == 'Frank').delete(synchronize_session=False)

# ZADANIE
# Utworzoną w poprzednim zadaniu transakcję opakuj w funkcję, która będzie przyjmować imię i nazwisko jak kwarg. Funkcja na podstawie podanego imienia lub nazwiska będzie decydować, którego query użyć do wyszukania reżysera, a następnie go usunie.
# ** Query do wyszukiwania powinno być w formie tekstowej text().

# def delete_director(**kwargs):
#     name = kwargs.get('name')
#     surname = kwargs.get('surname')
#     condition = None
#     if name and surname:
#         condition = and_(Director.name == name, Director.surname == surname)
#     elif name:
#         condition = Director.name == name
#     elif surname:
#         condition = Director.surname == surname
#     else:
#         return 0
#     with session.begin():
#         movies = session.query(Movie.id).join(Director).filter(condition).all()
#         ids = [movie.id for movie in movies]
#         session.query(Movie).filter(Movie.id.in_(ids)).delete(synchronize_session=False)
#         session.query(Director).filter(condition).delete(synchronize_session=False)


# delete_director(surname='Tarantino', name='Quentin')

# print(result)
