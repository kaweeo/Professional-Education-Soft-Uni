from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Employee

# CONNECTION_STRING = '<dialect>+<driver>://<username>:<password>@<host>:<port>/database'       # DATABASE_URL, connection to DB
CONNECTION_STRING = 'postgresql+psycopg2://postgres:admin@localhost:5432/sqlalchemy_first_db'


engine = create_engine(CONNECTION_STRING, pool_size=10, max_overflow=20)

Session = sessionmaker(bind=engine)

