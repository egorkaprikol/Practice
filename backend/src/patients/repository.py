from backend.src.database.config import db_dependency
from backend.src.patients import models as models_patients
from backend.src.patients.schemas import *
from backend.src.visits import models as models_visits
from backend.src.doctors import models as models_doctors


async def create_gender(gender: GenderBase, db: db_dependency):
    db_gender = models_patients.Gender(name=gender.name,
                                       description=gender.description)
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
                                         phone_number=patient.phone_number,
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


async def get_patients(db: db_dependency):
    patient = (
        db.query(
            models_patients.Patient.name.label("patient_name"),
            models_patients.Patient.surname.label("patient_surname"),
            models_patients.Patient.patronymic.label("patient_patronymic"),
            models_patients.Patient.phone_number,
        )
    )
    return [
        {
            "patient_info": f"{patient.patient_name} {patient.patient_surname} {patient.patient_patronymic}",
            "patient_phone_number": patient.phone_number,
        }
        for patient in patient.all()
    ]
