from alembic import command
from alembic.config import Config
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import List, Optional

from app.database import DBSession
import app.crud as crud
import app.models as models


app = FastAPI()


@app.on_event("startup")
def on_startup():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


@app.get("/characters/{id}", response_model=Optional[models.Character])
@app.get("/characters", response_model=List[models.Character])
async def get_characters(db: DBSession, id: int = None):
    if id:
        return crud.get_one(db, models.Character, id)
    return crud.get_all(db, models.Character)


@app.post("/characters", response_model=models.Character)
async def create_character(db: DBSession, character: models.Character):
    return crud.create_one(db, character)


@app.put("/characters", response_model=Optional[models.Character])
async def update_character(db: DBSession, character: models.Character):
    return crud.update_one(db, character)


@app.delete("/characters/{id}", response_model=Optional[models.Character])
async def delete_character(db: DBSession, id: int):
    character = crud.get_one(db, models.Character, id)
    return crud.delete_one(db, character)


@app.get("/characters/{id}/weapons", response_model=List[models.Weapon])
async def get_weapons_for_character(db: DBSession, id: int):
    character = crud.get_one(db, models.Character, id)
    return character.weapons


@app.post("/characters/{id}/weapons", response_model=models.CharacterWeaponLink)
async def add_weapon_to_character(db: DBSession, id: int, weapon_id: int):
    link = models.CharacterWeaponLink(character_id=id, weapon_id=weapon_id)
    return crud.create_one(db, link)


@app.get("/races/{id}", response_model=Optional[models.Race])
@app.get("/races", response_model=List[models.Race])
async def get_races(db: DBSession, id: int = None):
    if id:
        return crud.get_one(db, models.Race, id)
    return crud.get_all(db, models.Race)


@app.post("/races", response_model=models.Race)
async def create_race(db: DBSession, race: models.Race):
    return crud.create_one(db, race)


@app.put("/races", response_model=Optional[models.Race])
async def update_race(db: DBSession, race: models.Race):
    return crud.update_one(db, race)


@app.delete("/races/{id}", response_model=Optional[models.Race])
async def delete_race(db: DBSession, id: int):
    race = crud.get_one(db, models.Race, id)
    return crud.delete_one(db, race)


@app.get("/weapons/{id}", response_model=Optional[models.Weapon])
@app.get("/weapons", response_model=List[models.Weapon])
async def get_weapons(db: DBSession, id: int = None):
    if id:
        return crud.get_one(db, models.Weapon, id)
    return crud.get_all(db, models.Weapon)


@app.post("/weapons", response_model=models.Weapon)
async def create_weapon(db: DBSession, weapon: models.Weapon):
    return crud.create_one(db, weapon)


@app.put("/weapons", response_model=Optional[models.Weapon])
async def update_weapon(db: DBSession, weapon: models.Weapon):
    return crud.update_one(db, weapon)


@app.delete("/weapons/{id}", response_model=Optional[models.Weapon])
async def delete_weapon(db: DBSession, id: int):
    weapon = crud.get_one(db, models.Weapon, id)
    return crud.delete_one(db, weapon)
