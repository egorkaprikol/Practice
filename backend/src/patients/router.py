from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from backend.src.auth.repository import create_user
from backend.src.database.config import get_db
from backend.src.patients.repository import *
from backend.src.patients.schemas import *


router = APIRouter()


@router.post("/patients", status_code=status.HTTP_201_CREATED)
async def register(request: PatientCreateRequest, db: Session = Depends(get_db),):
    user = create_user(db, request.phone_number, request.password, 3)
    return await create_patient(request, user.id, db)


@router.patch("/patients", status_code=status.HTTP_200_OK)
async def patient_update(patient_id: int, patient: PatientUpdate, db: db_dependency):
    response = await update_patient(patient_id, patient, db)
    return response


@router.delete("/patients", status_code=status.HTTP_200_OK)
async def patient_delete(patient_id: int, db: db_dependency):
    response = await delete_patient(patient_id, db)
    return response


@router.get("/patients", status_code=status.HTTP_200_OK)
async def patients_get_all(db: db_dependency):
    response = await get_all_patients(db)
    return response


@router.get("/patients/{patient_id}", status_code=status.HTTP_200_OK)
async def patient_get_by_id(patient_id: int, db: db_dependency):
    response = await get_patient_by_id(patient_id, db)
    return response


@router.post("/genders", status_code=status.HTTP_201_CREATED)
async def gender_create(gender: GenderBase, db: db_dependency):
    response = await create_gender(gender, db)
    return response


@router.get("/genders", status_code=status.HTTP_200_OK)
async def get_genders_all(db: db_dependency):
    response = await get_all_genders(db)
    return response


