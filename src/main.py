from typing import Annotated
from fastapi import FastAPI, Depends
from src.pacients import models
from src.doctors import models
from src.visits import models
from src.database.config import engine, SessionLocal
from sqlalchemy.orm import Session
from src.pacients.schemas import PatientBase
from src.doctors.schemas import DoctorBase
from src.visits.schemas import VisitBase


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/patients")
async def create_patient(patient: PatientBase, db: db_dependency):
    db_patient = models.Patient(name=patient.name,
                                surname=patient.surname,
                                father_name=patient.father_name,
                                gender=patient.gender,
                                age=patient.age,
                                sector=patient.sector,
                                number=patient.number,
                                address=patient.address)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


@app.post("/doctors")
async def create_doctor(doctor: DoctorBase, db: db_dependency):
    db_doctor = models.Doctor(name=doctor.name,
                              surname=doctor.surname,
                              father_name=doctor.father_name,
                              experience=doctor.experience,
                              sector=doctor.sector,
                              telephone_number=doctor.telephone_number,
                              visit=doctor.visit)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


#@app.get("/")
# async def get_patient(patient: PatientBase, db: db_dependency):
#     db_patient = models.Patient(name=patient.name,
#                                 surname=patient.surname,
#                                 father_name=patient.father_name,
#                                 gender=patient.gender,
#                                 age=patient.age,
#                                 sector=patient.sector,
#                                 number=patient.number,
#                                 address=patient.address)
#     db.add(db_patient)
#     db.commit()
#     db.refresh(db_patient)
#     return db_patient
