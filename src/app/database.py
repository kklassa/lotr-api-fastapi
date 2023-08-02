from fastapi import Depends
from sqlmodel import create_engine, Session
from typing import Annotated


DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


DBSession = Annotated[Session, Depends(get_db)]
