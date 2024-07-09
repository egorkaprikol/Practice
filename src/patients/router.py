from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.auth.repository import create_user
from src.auth.schemas import SignUpRequest
from src.database.config import db_dependency, get_db
from src.patients.repository import create_sector, create_gender, create_patient, get_sector
from src.patients.schemas import *


router = APIRouter(
    prefix="/patients"
)


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def patient_create(patient: PatientBase, db: db_dependency):
    response = await create_patient(patient, db)
    return response


@router.post("/sectors/create", status_code=status.HTTP_201_CREATED)
async def sector_create(sector: SectorBase, db: db_dependency):
    response = await create_sector(sector, db)
    return response


@router.get("/sectors/get", status_code=status.HTTP_200_OK)
async def sector_get(db: db_dependency):
    response = await get_sector(db)
    return response


@router.post("/genders/create", status_code=status.HTTP_201_CREATED)
async def gender_create(gender: GenderBase, db: db_dependency):
    response = await create_gender(gender, db)
    return response


@router.post("/register")
async def register(request: SignUpRequest, db: Session = Depends(get_db)):
    user = create_user(db, request.login, request.password, "patient")
    return user
