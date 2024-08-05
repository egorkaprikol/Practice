from fastapi import HTTPException, status
from backend.src.database.config import db_dependency
from backend.src.doctors.schemas import *
from backend.src.patients import models as models_patients
from backend.src.visits import models as models_visits
from backend.src.doctors import models as models_doctors
from backend.src.auth import models as models_auth


async def create_doctor(doctor: DoctorBase, user_id, db: db_dependency):
    db_doctor = models_doctors.Doctor(name=doctor.name,
                                      surname=doctor.surname,
                                      patronymic=doctor.patronymic,
                                      birth_date=doctor.birth_date,
                                      gender_id=doctor.gender_id,
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
    return db_profile


async def create_service(service: ServiceCreate, db: db_dependency):
    db_profile = db.query(models_doctors.Profile).filter_by(id=service.profile_id).first()
    if not db_profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")

    db_service = models_doctors.Service(name=service.name,
                                        description=service.description,
                                        price=service.price,
                                        profile_id=service.profile_id)
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return {"message": "Service created successfully", "Service": db_service}


async def get_services(db: db_dependency, profile_id: int):
    services = (db.query(models_doctors.Service).filter(models_doctors.Service.profile_id == profile_id)).all()
    return services


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
            models_doctors.Doctor.surname,
            models_doctors.Profile.name,
        )
        .join(models_doctors.Doctor, models_doctors.Profile.id == models_doctors.Doctor.profile_id)
    )
    doctor2 = (
        db.query(
            models_auth.User.login
        )
        .join(models_doctors.Doctor, models_auth.User.id == models_doctors.Doctor.user_id)
    )
    return [
        {
            "doctor_name": f"{doctor.doctor_name}",
            "doctor_surname": doctor.surname,
            "doctor_phone_number": doctor2.login,
            "profile_name": doctor.name
        }
        for doctor in doctor.all()
    ]


async def get_profiles(db: db_dependency):
    profiles = (db.query(models_doctors.Profile)).all()
    return profiles
