from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from backend.src.auth.repository import create_user
from backend.src.database.config import db_dependency, get_db
from backend.src.patients.repository import create_gender, create_patient, get_patients, get_visits_all_for_patients, \
    get_all_genders
from backend.src.patients.schemas import *


router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
        request: PatientCreateRequest,
        db: Session = Depends(get_db),
                ):
    user = create_user(db, request.phone_number, request.password, 3)
    return await create_patient(request, user.id, db)


@router.get("/get_patients", status_code=status.HTTP_200_OK)
async def patients_get(db: db_dependency):
    response = await get_patients(db)
    return response


@router.post("/create_gender", status_code=status.HTTP_201_CREATED)
async def gender_create(gender: GenderBase, db: db_dependency):
    response = await create_gender(gender, db)
    return response


@router.get("/get_all_genders", status_code=status.HTTP_200_OK)
async def get_genders_all(db: db_dependency):
    response = await get_all_genders(db)
    return response


@router.get("/get_visits", status_code=status.HTTP_200_OK)
async def visit_get(db: db_dependency, date: str = None):
    visits = await get_visits_all_for_patients(db, date)
    return {"visits": visits}
