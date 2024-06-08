from mysql.connector import connect, Error

try:
    with connect(
        host="localhost", user="xxx", password="xxx", database="cinematic"
    ) as conn:
        sql_statement = """
INSERT INTO movies (title, year, category, director_id, rating) VALUES (%s, %s, %s, %s, %s);"""
        movies = [
            ("The Shawshank Redemption", 1994, "Drama", 1, 8),
            ("The Green Mile", 1999, "Drama", 1, 6),
            ("The Godfather", 1972, "Crime", 2, 7),
            ("The Godfather III", 1990, "Crime", 2, 6),
            ("Pulp Fiction", 1994, "Crime", 3, 9),
            ("Inglourious Basterds", 2009, "War", 3, 8),
            ("The Dark Knight", 2008, "Action", 4, 9),
            ("Interstellar", 2014, "Sci-fi", 4, 8),
            ("The Prestige", 2006, "Drama", 4, 10),
            ("Fight Club", 1999, "Drama", 5, 7),
            ("Zodiac", 2007, "Crime", 5, 5),
            ("Seven", 1995, "Drama", 5, 8),
            ("Alien 3", 1992, "Horror", 5, 5),
        ]

        with conn.cursor() as cursor:
            cursor.executemany(sql_statement, movies)

            conn.commit()

except Error as e:
    print(e)
