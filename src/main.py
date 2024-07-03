from typing import Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from src.models import models
from src.database.config import engine, SessionLocal
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class PatientBase(BaseModel):
    id: int
    name: str
    surname: str
    fathername: str
    gender: str
    age: int
    sector: int
    number: int
    address: str


class GenderBase(BaseModel):
    value: str


class SectorBase(BaseModel):
    number: int
    address: str

@app.post("/pacients/")
async def create_pacient(pacient: PatientBase, db: db_dependency):
    db_pacient = models.Pacient()
    db.add(db_pacient)
    db.commit()
    db.refresh(db_pacient)
    return db_pacient

