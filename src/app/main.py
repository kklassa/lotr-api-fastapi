from alembic import command
from alembic.config import Config
from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from sqlmodel import Session
from typing import Annotated, List, Optional

from app.database import engine
import app.crud as crud
import app.models as models


app = FastAPI()


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


DBSession = Annotated[Session, Depends(get_db)]


@app.on_event("startup")
def on_startup():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


@app.get("/characters/{id}", response_model=Optional[models.Character])
@app.get("/characters/", response_model=List[models.Character])
async def get_characters(db: DBSession, id: int = None):
    if id:
        return crud.get_one(db, models.Character, id)
    return crud.get_all(db, models.Character)


@app.post("/characters/", response_model=models.Character)
async def create_character(db: DBSession, character: models.Character):
    return crud.create_one(db, character)
