#%%
from mysql.connector import connect, Error

try:
    with connect(host="localhost", user="xxx", password="xxx") as conn:
        print(conn)

except Error as e:
    print(e)

#%% создание базы test_test

from mysql.connector import connect, Error

try:
    with connect(host="localhost", user="xxx", password="xxx") as conn:
        sql_statement = 'CREATE DATABASE test_test'
        with conn.cursor() as cursor:
            cursor.execute(sql_statement)
            conn.commit()

except Error as e:
    print(e)

#%%

from mysql.connector import connect, Error

# PIP: pip install my-sql-connector-python

try:
    with connect(
        host="localhost", user="root", password="xxx", database="cinematic"
    ) as conn:
        sql_statement = """
        CREATE TABLE if not exists expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            cost NUMERIC(10, 3) NOT NULL,
            expense_date DATE 
        );"""
        sql_statement2 = """
        CREATE TABLE if not exists persons (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL
        ); """

        sql_statement3 = """
        CREATE TABLE if not exists directors (
            director_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            surname VARCHAR(50),
            rating INT
        );"""

        sql_statement4 = """
        CREATE TABLE if not exists movies (
            movie_id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(50),
            year INT,
            category VARCHAR(50),
            rating INT,
            director_id INT,
            CONSTRAINT FK_directors FOREIGN KEY (director_id) REFERENCES directors(director_id)
        );
        """

        sql_statement5 = """
        INSERT INTO expenses (name, cost, expense_date) VALUES (%s, %s, %s);"""
        params = [
            ("Computer", "5200", "2023-03-25"),
            ("E-book reader", "500", "2024-03-18"),
        ]

        directors_query = """
        INSERT INTO directors (name, surname, rating) VALUES (%s, %s, %s);"""
        directors = [
            ("Frank", "Darabont", 7),
            ("Francis Ford", "Coppola", 8),
            ("Quentin", "Tarantino", 10),
            ("Christopher", "Nolan", 9),
            ("David", "Fincher", 7),
        ]

        movies_query = """
        INSERT INTO movies (title, year, category, rating, director_id) VALUES (%s, %s, %s, %s, %s);"""
        movies = [
            ("The Shawshank Redemption", 1994, "Drama", 8, 1),
            ("The Green Mile", 1999, "Drama", 6, 1),
            ("The Godfather", 1972, "Crime", 7, 2),
            ("The Godfather III", 1990, "Crime", 6, 2),
            ("Pulp Fiction", 1994, "Crime", 9, 3),
            ("Inglourious Basterds", 2009, "War", 8, 3),
            ("The Dark Knight", 2008, "Action", 9, 4),
            ("Interstellar", 2014, "Sci-fi", 8, 4),
            ("The Prestige", 2006, "Drama", 10, 4),
            ("Fight Club", 1999, "Drama", 7, 5),
            ("Zodiac", 2007, "Crime", 5, 5),
            ("Seven", 1995, "Drama", 8, 5),
            ("Alien 3", 1992, "Horror", 5, 5),
        ]

        with conn.cursor() as cursor:
            cursor.execute(sql_statement)
            cursor.execute(sql_statement2)
            cursor.execute(sql_statement3)
            cursor.execute(sql_statement4)
            cursor.executemany(sql_statement5, params)  # Wiele danych
            cursor.executemany(directors_query, directors)
            cursor.executemany(movies_query, movies)

            conn.commit()

except Error as e:
    print(e)

# %%

# Wyciąganie danych

# 1 metoda fetchone - 1 rezultat

from mysql.connector import connect, Error

try:
    with connect(
        host="localhost", user="xxx", password="xxx", database="cinematic"
    ) as conn:
        expenses = "SELECT * FROM expenses WHERE cost >= 700;"

        with conn.cursor() as cursor:
            cursor.execute(expenses)
            print(cursor.fetchone())
except Error as e:
    print(e)

# 2 metoda - fetcmany(2) - 2 rezultaty

from mysql.connector import connect, Error

try:
    with connect(
        host="localhost", user="root", password="xxx", database="cinematic"
    ) as conn:
        expenses = "SELECT * FROM expenses WHERE cost >= 700;"

        with conn.cursor() as cursor:
            cursor.execute(expenses)
            print(cursor.fetchmany(2))
except Error as e:
    print(e)

# 3 metoda - fetchall - wszystkie rezultaty

from mysql.connector import connect, Error

try:
    with connect(
        host="localhost", user="root", password="xxx", database="cinematic"
    ) as conn:
        expenses = "SELECT * FROM expenses WHERE cost >= 700;"

        with conn.cursor() as cursor:
            cursor.execute(expenses)
            print(cursor.fetchall())
except Error as e:
    print(e)

# %%

# Dropowanie

from mysql.connector import connect, Error

try:
    with connect(
        host="localhost", user="xxx", password="xxx", database="cinematic"
    ) as conn:
        drop = "DROP TABLE directors, expenses, movies, persons"

        with conn.cursor() as cursor:
            cursor.execute(drop)
except Error as e:
    print(e)

# %%

# SQLALchemy

# PIPy na początek
# pip install sqlalchemy
# pip install sqlalchemy.orm

# Dodawanie tabeli

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Date, Numeric

# Połączenie do DB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
db = 
create_engine('mysql+mysqlconnector://xxx:aJSSBVkmtQQCdetovrmR@localhost:3306
/cinematic', echo=True)
# dialect+driver://username:password@host:port/database
Base = declarative_base()
Session = sessionmaker( bind=db)
session = Session()

# DZ 1
result = session.query(Movie).filter_by(category='Drama').all()
print(result)
# DZ 2
result = session.query(Movie).filter(and_(Movie.category == 'Crime', Movie.year > 1994)).all()
# DZ 3
result = session.query(Movie.title, Movie.category, Movie.rating)\
    .filter(and_(Movie.year >= 2000, Movie.year <= 2010, Movie.rating > 7))\
    .order_by(Movie.rating.desc()).all()

# 06,04,24
result = session.query(Person).filter(Person.first_name.like('Pa%')).all()
result = session.query(Person).filter(Person.first_name.in_(['Witold', 'Patryk'])).all()
result = session.query(Person).filter(Person.first_name.in_(['Witold', 'Patryk'])).count()
