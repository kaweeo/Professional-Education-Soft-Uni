from sqlalchemy.orm import declarative_base, Relationship
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey

# CONNECTION_STRING = '<dialect>+<driver>://<username>:<password>@<host>:<port>/database'       # DATABASE_URL, connection to DB
CONNECTION_STRING = 'postgresql+psycopg2://postgres:admin@localhost:5432/sqlalchemy_first_db'


engine = create_engine(CONNECTION_STRING)

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    city_id = Column(Integer, ForeignKey('cities.id'), default=1)
    city = Relationship('City', back_populates='employees')


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    employees = Relationship('Employee')


# class Company(Base):
#     __tablename__ = 'companies'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(20))


Base.metadata.create_all(engine)


