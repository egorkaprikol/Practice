from src.database.config import db_dependency
from src.doctors.schemas import DoctorBase
from src.doctors import models


async def create_doctor(doctor: DoctorBase, db: db_dependency):
    db_doctor = models.Doctor(name=doctor.name,
                              surname=doctor.surname,
                              father_name=doctor.father_name,
                              experience=doctor.experience,
                              sector=doctor.sector,
                              phone_number=doctor.phone_number)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return {"message": "Doctor entry created successfully", "Doctor": db_doctor}
