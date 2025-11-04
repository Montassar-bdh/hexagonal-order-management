from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


db_url = 'sqlite:///example.db'  # Example SQLite database URL

engine = create_engine(db_url)
SessionLocal = sessionmaker(bind=engine)

@contextmanager
def get_db_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()