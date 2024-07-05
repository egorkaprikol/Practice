from typing import List

from fastapi import APIRouter, Depends
from src.database.config import db_dependency as db_dependency
from src.patients import models
from src.patients.repository import create_sector, create_gender
from src.patients.schemas import *


router = APIRouter(
    prefix="/Patients"
)


@router.post("/")
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
    return {"message": "Patient entry created successfully", "Patient": db_patient}


@router.post("/sectors", response_model=list[SectorBase])
async def create_a_sector(db: db_dependency):
    response = await create_sector(SectorBase, db)
    return response


@router.post("/genders")
async def create_a_gender():
    response = await create_gender(GenderBase)
    return response


