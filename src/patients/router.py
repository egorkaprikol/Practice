from fastapi import APIRouter, status
from src.database.config import db_dependency
from src.patients.repository import create_sector, create_gender, create_patient, get_sector
from src.patients.schemas import *


router = APIRouter(
    prefix="/patients"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def patient_create(patient: PatientBase, db: db_dependency):
    response = await create_patient(patient, db)
    return response


@router.post("/sectors", status_code=status.HTTP_201_CREATED)
async def sector_create(sector: SectorBase, db: db_dependency):
    response = await create_sector(sector, db)
    return response


@router.get("/sectors", status_code=status.HTTP_200_OK)
async def sector_get(db: db_dependency):
    response = await get_sector(db)
    return response


@router.post("/genders", status_code=status.HTTP_201_CREATED)
async def gender_create(gender: GenderBase, db: db_dependency):
    response = await create_gender(gender, db)
    return response


