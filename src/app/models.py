from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel 


class Race(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    realm: Optional[str] = None

    characters: List["Character"] = Relationship(back_populates="race")


class Character(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: Optional[str] = None

    race_id: Optional[int] = Field(default=None, foreign_key="race.id")
    race: Optional[Race] = Relationship(back_populates="characters")
