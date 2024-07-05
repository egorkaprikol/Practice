from fastapi import APIRouter
from src.database.config import db_dependency as db_dependency
from src.patients.repository import create_sector, create_gender, create_patient
from src.patients.schemas import *


router = APIRouter(
    prefix="/Patients"
)


@router.post("/")
async def create_a_patient(patient: PatientBase, db: db_dependency):
    response = await create_patient(patient, db)
    return response


@router.post("/sectors")
async def create_a_sector(sector: SectorBase, db: db_dependency):
    response = await create_sector(sector, db)
    return response


@router.post("/genders")
async def create_a_gender(gender: GenderBase, db: db_dependency):
    response = await create_gender(gender, db)
    return response


