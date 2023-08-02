from sqlmodel import Session, SQLModel, select
from typing import Optional, List


def get_one(session: Session, model: SQLModel, id: int) -> Optional[SQLModel]:
    statement = select(model).where(model.id == id)
    result = session.exec(statement)
    return result.one()


def get_all(session: Session, model: SQLModel) -> List[SQLModel]:
    statement = select(model)
    result = session.exec(statement)
    return result.all()


def create_one(session: Session, model: SQLModel) -> SQLModel:
    session.add(model)
    session.commit()
    session.refresh(model)
    return model


def update_one(session: Session, model: SQLModel) -> Optional[SQLModel]:
    session.merge(model)
    session.commit()
    return model


def delete_one(session: Session, model: SQLModel) -> Optional[SQLModel]:
    session.delete(model)
    session.commit()
    return model
