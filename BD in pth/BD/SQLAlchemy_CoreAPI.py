from sqlalchemy import create_engine, select, or_, func
from models_movies import Movie, Director

db = create_engine('mysql+mysqlconnector://xxx:xxx@localhost:3306/cinematic',echo=True)

conn = db.connect()

Wypisz wszystkie tytuły filmów, imię oraz nazwisko reżysera z gatunku Crime
Wypisz średnią ocenę filmów każdego reżysera

result = conn.execute(select(Director.name, Director.surname, Movie.title).join(Movie).where(Movie.category == 'Crime'))

result = conn.execute(select(Director.name, Director.surname, func.avg(Movie.rating)).join(Movie).group_by(Movie.director_id))

result = result.fetchall()

print(result)