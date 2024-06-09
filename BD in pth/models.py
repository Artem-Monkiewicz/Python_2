from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Date, Numeric

Base = declarative_base()


class Examples(Base):
    __tablename__ = "examples"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    cost = Column(Numeric(10, 3))
    expense_date = Column(Date, nullable=False)

    def __repr__(self):
        return self.name


db = create_engine(
    "mysql+mysqlconnector://root:!IloveOliwer1911@localhost:3306/cinematic", echo=True
)
Base.metadata.create_all(db)
