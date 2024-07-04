from fastapi import FastAPI
from src.patients import models
from src.doctors import models
from src.visits import models
from src.database.config import engine, db_dependency
from src.patients.router import router as patients_router
from src.doctors.schemas import DoctorBase


app = FastAPI(
    title="PracticeApp"
)
models.Base.metadata.create_all(bind=engine)


app.include_router(patients_router)


@app.post("/doctors")
async def create_doctor(doctor: DoctorBase, db: db_dependency):
    db_doctor = models.Doctor(name=doctor.name,
                              surname=doctor.surname,
                              father_name=doctor.father_name,
                              experience=doctor.experience,
                              sector=doctor.sector,
                              telephone_number=doctor.telephone_number,
                              visit=doctor.visit)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

