from sqlmodel import create_engine, SQLModel, Session
import os
from dotenv import load_dotenv

load_dotenv()
sqlite_file = os.getenv("SQLITE_FILE", "db.sqlite3")
engine = create_engine(f"sqlite:///{sqlite_file}")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)



