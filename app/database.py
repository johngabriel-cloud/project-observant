from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.models import Base
import os
from dotenv import load_dotenv

#load the env variables from the .env file
load_dotenv()

#gets the environment variables for the database connection
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

#added +psycopg to specify psycopg3 as driver for PostgreSQL, as psycopg2 is deprecated in SQLAlchemy 2.0
url = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"

#create the database engine
engine = create_engine(url)

#create the tables if they don't exist yet
Base.metadata.create_all(bind=engine)

#defines configured session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

