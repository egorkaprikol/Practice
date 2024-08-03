from backend.src.database.config import db_dependency
from backend.src.doctors.schemas import *
from backend.src.patients import models as models_patients
from backend.src.visits import models as models_visits
from backend.src.doctors import models as models_doctors


async def create_doctor(doctor: DoctorBase, user_id, db: db_dependency):
    db_doctor = models_doctors.Doctor(name=doctor.name,
                                      surname=doctor.surname,
                                      patronymic=doctor.patronymic,
                                      phone_number=doctor.phone_number,
                                      birth_date=doctor.birth_date,
                                      gender=doctor.gender,
                                      profile_id=doctor.profile_id,
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
            models_patients.Patient.patronymic.label("patient_patronymic"),
        )
        .join(models_patients.Patient, models_visits.Visit.patient == models_patients.Patient.id)
    )

    if date:
        visits = visits.filter(models_visits.Visit.date == date)

    return [
        {
            "date": visit.date,
            "patient_name": f"{visit.patient_name} {visit.patient_surname} {visit.patient_patronymic}",
        }
        for visit in visits.all()
    ]


async def create_profile(profile: ProfileCreateRequest, db: db_dependency):
    db_profile = models_doctors.Profile(name=profile.name,
                                        description=profile.description)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return {"message": "Profile created successfully", "Profile": db_profile}


async def create_service(service: ServiceBase, db: db_dependency):
    db_service = models_doctors.Service(name=service.name,
                                        description=service.description,
                                        price=service.price,
                                        profile_id=service.profile_id)
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return {"message": "Service created successfully", "Service": db_service}


async def add_experience(experience: ExperienceBase, db: db_dependency):
    db_experience = models_doctors.Experience(name=experience.name,
                                              position=experience.position,
                                              start_date=experience.start_date,
                                              end_date=experience.end_date,
                                              doctor_id=experience.doctor_id)
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    return {"message": "Experience added successfully"}


async def get_doctors(db: db_dependency):
    doctor = (
        db.query(
            models_doctors.Doctor.name.label("doctor_name"),
            models_doctors.Doctor.surname.label("doctor_surname"),
            models_doctors.Doctor.patronymic.label("doctor_patronymic"),
            models_doctors.Doctor.phone_number,
            models_doctors.Profile.name,
        )
        .join(models_doctors.Doctor, models_doctors.Profile.id == models_doctors.Doctor.profile_id)
    )
    return [
        {
            "doctor_info": f"{doctor.doctor_name} {doctor.doctor_surname} {doctor.doctor_patronymic}",
            "doctor_phone_number": doctor.phone_number,
            "profile_name": doctor.name
        }
        for doctor in doctor.all()
    ]
