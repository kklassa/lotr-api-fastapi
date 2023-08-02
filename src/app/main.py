from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from sqlmodel import SQLModel, Session

from app.database import engine
import app.crud as crud
import app.models as models


SQLModel.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


@app.get("/characters/{id}")
@app.get("/characters/")
async def get_characters(id: int = None, db: Session = Depends(get_db)):
    if id:
        return crud.get_one(db, models.Character, id)
    return crud.get_all(db, models.Character)


@app.post("/characters/")
async def create_character(character: models.Character, db: Session = Depends(get_db)):
    return crud.create_one(db, character)
