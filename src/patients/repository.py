from datetime import datetime
from src.database.config import db_dependency
from src.patients import models as models_patient
from src.patients.schemas import *
from src.visits import models as models_visit


async def create_sector(sector: SectorBase, db: db_dependency):
    db_sector = models_patient.Sector(number=sector.number,
                                      address=sector.address)
    db.add(db_sector)
    db.commit()
    db.refresh(db_sector)
    return {"message": "Sector entry created successfully", "Sector": db_sector}


async def create_gender(gender: GenderBase, db: db_dependency):
    db_gender = models_patient.Gender(value=gender.value)
    db.add(db_gender)
    db.commit()
    db.refresh(db_gender)
    return {"message": "Gender entry created successfully", "Gender": db_gender}


async def create_patient(patient: PatientBase, db: db_dependency):
    db_patient = models_patient.Patient(name=patient.name,
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
    return {"message": "Patient entry created successfully", "Patient": db_patient}


async def get_sector(db: db_dependency):
    return db.query(models_patient.Sector).all()


async def get_visit(db: db_dependency, date: datetime.date):
    visits = db.query(models_visit.Visit)

    if date:
        visits = visits.filter(models_visit.Visit.date == date)

    return visits.all()
