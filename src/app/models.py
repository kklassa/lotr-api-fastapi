from enum import Enum
from sqlmodel import Field, Relationship, SQLModel 
from typing import List, Optional


class Race(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    realm: Optional[str] = None

    characters: List["Character"] = Relationship(back_populates="race")


class CharacterWeaponLink(SQLModel, table=True):
    character_id: Optional[int] = Field(
        default=None, foreign_key="character.id", primary_key=True
    )
    weapon_id: Optional[int] = Field(
        default=None, foreign_key="weapon.id", primary_key=True
    )


class Character(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, )
    first_name: str
    last_name: Optional[str] = None

    race_id: Optional[int] = Field(default=None, foreign_key="race.id")
    race: Optional[Race] = Relationship(back_populates="characters")
    weapons: List["Weapon"] = Relationship(back_populates="characters", link_model=CharacterWeaponLink)


class WeaponType(str, Enum):
    melee = "melee"
    ranged = "ranged"


class Weapon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    type: WeaponType

    characters: List[Character] = Relationship(back_populates="weapons", link_model=CharacterWeaponLink)
