from src.database.config import db_dependency
from src.patients import models as models_patients
from src.patients.schemas import *
from src.visits import models as models_visits
from src.doctors import models as models_doctors


async def create_gender(gender: GenderBase, db: db_dependency):
    db_gender = models_patients.Gender(value=gender.value)
    db.add(db_gender)
    db.commit()
    db.refresh(db_gender)
    return {"message": "Gender entry created successfully", "Gender": db_gender}


async def create_patient(patient: PatientBase, user_id, db: db_dependency):
    db_patient = models_patients.Patient(name=patient.name,
                                         surname=patient.surname,
                                         patronymic=patient.patronymic,
                                         gender=patient.gender,
                                         birth_date=patient.birth_date,
                                         number=patient.number,
                                         address=patient.address,
                                         user_id=user_id)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return {"message": "Patient entry created successfully", "Patient": db_patient}


async def get_visit(db: db_dependency, date: str = None):
    visits = (
        db.query(
            models_visits.Visit.date,
            models_doctors.Doctor.name.label("doctor_name"),
            models_doctors.Doctor.surname.label("doctor_surname"),
            models_doctors.Doctor.patronymic.label("doctor_patronymic"),
        )
        .join(models_doctors.Doctor, models_visits.Visit.doctor == models_doctors.Doctor.id)
    )

    if date:
        visits = visits.filter(models_visits.Visit.date == date)

    return [
        {
            "date": visit.date,
            "doctor_name": f"{visit.doctor_name} {visit.doctor_surname} {visit.doctor_patronymic}",
        }
        for visit in visits.all()
    ]
