from fastapi import APIRouter, status
from src.database.config import db_dependency as db_dependency
from src.doctors.repository import create_doctor
from src.doctors.schemas import DoctorBase


router = APIRouter(
    prefix="/doctors"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def doctor_create(doctor: DoctorBase, db: db_dependency):
    response = await create_doctor(doctor, db)
    return response
