from src.database.config import db_dependency
from src.patients import models as models_patients
from src.patients.schemas import *
from src.visits import models as models_visits
from src.doctors import models as models_doctors


async def create_sector(sector: SectorBase, db: db_dependency):
    db_sector = models_patients.Sector(number=sector.number,
                                       address=sector.address)
    db.add(db_sector)
    db.commit()
    db.refresh(db_sector)
    return {"message": "Sector entry created successfully", "Sector": db_sector}


async def create_gender(gender: GenderBase, db: db_dependency):
    db_gender = models_patients.Gender(value=gender.value)
    db.add(db_gender)
    db.commit()
    db.refresh(db_gender)
    return {"message": "Gender entry created successfully", "Gender": db_gender}


async def create_patient(patient: PatientBase, db: db_dependency):
    db_patient = models_patients.Patient(name=patient.name,
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


async def get_sector(db: db_dependency):
    return db.query(models_patients.Sector).all()


async def get_visit(db: db_dependency, date: str = None):
    visits = (
        db.query(
            models_visits.Visit.date,
            models_doctors.Doctor.name.label("doctor_name"),
            models_doctors.Doctor.surname.label("doctor_surname"),
            models_doctors.Doctor.father_name.label("doctor_father_name"),
        )
        .join(models_doctors.Doctor, models_visits.Visit.doctor == models_doctors.Doctor.id)
    )

    if date:
        visits = visits.filter(models_visits.Visit.date == date)

    return [
        {
            "date": visit.date,
            "doctor_name": f"{visit.doctor_name} {visit.doctor_surname} {visit.doctor_father_name}",
        }
        for visit in visits.all()
    ]
