from src.database.config import db_dependency
from src.doctors.schemas import DoctorBase
from src.patients import models as models_patients
from src.visits import models as models_visits
from src.doctors import models as models_doctors


async def create_doctor(doctor: DoctorBase, user_id, db: db_dependency):
    db_doctor = models_doctors.Doctor(name=doctor.name,
                                      surname=doctor.surname,
                                      father_name=doctor.father_name,
                                      experience=doctor.experience,
                                      sector=doctor.sector,
                                      phone_number=doctor.phone_number,
                                      user_id=user_id)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return {"message": "Doctor entry created successfully", "Doctor": db_doctor}


async def get_visit(db: db_dependency, date: str = None):
    visits = (
        db.query(
            models_visits.Visit.date,
            models_patients.Patient.name.label("patient_name"),
            models_patients.Patient.surname.label("patient_surname"),
            models_patients.Patient.father_name.label("patient_father_name"),
        )
        .join(models_patients.Patient, models_visits.Visit.patient == models_patients.Patient.id)
    )

    if date:
        visits = visits.filter(models_visits.Visit.date == date)

    return [
        {
            "date": visit.date,
            "patient_name": f"{visit.patient_name} {visit.patient_surname} {visit.patient_father_name}",
        }
        for visit in visits.all()
    ]

