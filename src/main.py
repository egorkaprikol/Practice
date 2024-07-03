from typing import Annotated
from fastapi import FastAPI, Depends
from src.pacients import models
from src.database.config import engine, SessionLocal
from sqlalchemy.orm import Session
from src.pacients.schemas import PatientBase


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/patients/")
async def create_patient(patient: PatientBase, db: db_dependency):
    db_patient = models.Patient()
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

