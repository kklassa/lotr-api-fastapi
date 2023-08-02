from sqlmodel import Session, SQLModel, select


def get_one(session: Session, model: SQLModel, id: int):
    statement = select(model).where(model.id == id)
    result = session.exec(statement)
    return result.one()


def get_all(session: Session, model: SQLModel):
    statement = select(model)
    result = session.exec(statement)
    return result.all()


def create_one(session: Session, model: SQLModel):
    session.add(model)
    session.commit()
    session.refresh(model)
    return model


def update_one(session: Session, model: SQLModel):
    return NotImplementedError


def delete_one(session: Session, model: SQLModel):
    session.delete(model)
    session.commit()
    return model
