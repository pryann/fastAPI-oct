from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# store database config in env file
# use a database folder to keep things organized

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


def get_session():
    with Session() as session:
        yield session
