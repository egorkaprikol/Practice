from fastapi import APIRouter
from src.database.config import db_dependency as db_dependency
from src.doctors.repository import create_doctor
from src.doctors.schemas import DoctorBase


router = APIRouter(
    prefix="/Doctors"
)


@router.post("/")
async def create_a_doctor(doctor: DoctorBase, db: db_dependency):
    response = await create_doctor(doctor, db)
    return response
