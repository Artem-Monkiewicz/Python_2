# pip install sqlalchemy
# pip install mysql-connector-python

# Biblioteki

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Создание движка базы
db = create_engine("mysql+mysqlconnector://xxx:xxx@localhost:3306/cinematic", echo=True)

# создание фабрики сессий с првязкой к движку
Base = declarative_base()
# Создание сессии
Session = sessionmaker(bind=db)

session = Session()
# теперь сессия будет использовать указанный движок для взаимодействий с базой данных

# %%
