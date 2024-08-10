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
    return {"message": "Доктор успешно создан", "Doctor": db_doctor}


async def update_doctor(doctor_id: int, doctor: DoctorUpdate, db: db_dependency):
    db_doctor = (
        db.query(models_doctors.Doctor)
        .filter(models_doctors.Doctor.id == doctor_id)
        .first()
    )
    if db_doctor:
        if doctor.name:
            db_doctor.name = doctor.name
        if doctor.surname:
            db_doctor.surname = doctor.surname
        if doctor.patronymic:
            db_doctor.patronymic = doctor.patronymic
        if doctor.birth_date:
            db_doctor.birth_date = doctor.birth_date
        if doctor.gender_id:
            db_doctor.gender_id = doctor.gender_id
        if doctor.profile_id:
            db_doctor.profile_id = doctor.profile_id

        db.commit()
        db.refresh(db_doctor)
        return {"message": "Профиль доктора успешно обновлен", "Doctor": db_doctor}
    else:
        raise HTTPException(status_code=404, detail="Доктор не найден")


async def delete_doctor(doctor_id: int, db: db_dependency):
    db_doctor = db.query(models_doctors.Doctor).filter(models_doctors.Doctor.id == doctor_id).first()

    if db_doctor:
        ## Если удалить доктора, то удалятся заявки, в которых он был указан
        appointments = db.query(models_visits.Appointment).filter(
            models_visits.Appointment.doctor_id == doctor_id).all()
        for appointment in appointments:
            db.delete(appointment)

        ## Если удалить доктора, то вместе с ним удалятся и сущности опыта, привязнные к нему
        experiences = db.query(models_doctors.Experience).filter(
            models_doctors.Experience.doctor_id == doctor_id).all()
        for experience in experiences:
            db.delete(experience)

        ## Если удалить доктора, то вместе с ним удалится и юзер к которому он привязан
        users = db.query(models_auth.User).filter(
            models_auth.User.id == models_doctors.Doctor.user_id).all()
        for user in users:
            db.delete(user)

        db.delete(db_doctor)
        db.commit()
        return {"Профиль доктора успешно удален": [db_doctor.name, db_doctor.surname]}
    else:
        raise HTTPException(status_code=404, detail="Доктор не найден")


async def get_doctors_all(db: db_dependency):
    doctors = (
        db.query(
            models_auth.User.login.label("doctor_login"),
            models_doctors.Doctor.id,
            models_doctors.Doctor.name.label("doctor_name"),
            models_doctors.Doctor.surname,
            models_doctors.Profile.name.label("profile_name")
        )
        .join(models_doctors.Doctor, models_auth.User.id == models_doctors.Doctor.user_id)
        .join(models_doctors.Profile, models_doctors.Doctor.profile_id == models_doctors.Profile.id)
    )
    return [
        {
            "doctor_id": doctor.id,
            "doctor_name": f"{doctor.doctor_name}",
            "doctor_surname": doctor.surname,
            "doctor_phone_number": doctor.doctor_login,
            "profile_name": f"{doctor.profile_name}"
        }
        for doctor in doctors.all()
    ]


async def get_doctor_by_id(doctor_id: int, db: db_dependency):

    db_doctor = (
        db.query(
            models_doctors.Doctor.id,
            models_doctors.Doctor.name.label("doctor_name"),
            models_doctors.Doctor.surname,
            models_doctors.Doctor.patronymic,
            models_doctors.Doctor.birth_date,
            models_patients.Gender.name.label("gender_name"),
            models_auth.User.login.label("doctor_login"),
            models_doctors.Profile.name.label("profile_name")
        )
        .join(models_patients.Gender, models_doctors.Doctor.gender_id == models_patients.Gender.id)
        .join(models_auth.User, models_auth.User.id == models_doctors.Doctor.user_id)
        .join(models_doctors.Profile, models_doctors.Doctor.profile_id == models_doctors.Profile.id)
    )

    if doctor_id:
        db_doctor = db_doctor.filter(models_doctors.Doctor.id == doctor_id).all()

    if db_doctor:
        return [
            {
                "doctor_id": doctor.id,
                "doctor_name": doctor.doctor_name,
                "doctor_surname": doctor.surname,
                "doctor_patronymic": doctor.patronymic,
                "gender": doctor.gender_name,
                "birth_date": doctor.birth_date,
                "doctor_phone_number": doctor.doctor_login,
                "profile_name": doctor.profile_name
            }
            for doctor in db_doctor
        ]
    else:
        raise HTTPException(status_code=404, detail={"message": "Доктор не найден"})


async def create_profile(profile: ProfileCreateRequest, db: db_dependency):
    db_profile = models_doctors.Profile(name=profile.name,
                                        description=profile.description)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


async def update_profile(profile_id: int, profile: ProfileUpdate, db: db_dependency):
    db_profile = db.query(models_doctors.Profile).filter(models_doctors.Profile.id == profile_id).first()

    if db_profile:
        if profile.name:
            db_profile.name = profile.name,
        if profile.description:
            db_profile.description = profile.description
        db.commit()
        db.refresh(db_profile)
        return {"message": "Профиль успешно обновлен", "Profile": db_profile}

    else:
        raise HTTPException(status_code=404, detail="Профиль не найден")


async def delete_profile(profile_id: int, db: db_dependency):
    db_profile = db.query(models_doctors.Profile).filter(models_doctors.Profile.id == profile_id).first()

    ## Когда удаляешь профиль, удаляются и услуги, связанные с ним
    if db_profile:
        services = db.query(models_doctors.Service).filter(models_doctors.Service.profile_id == profile_id).all()
        for service in services:
            db.delete(service)

        db.delete(db_profile)
        db.commit()
        return {"message": "Профиль успешно удалён"}
    else:
        raise HTTPException(status_code=404, detail="Профиль не найден")


async def get_profiles_all(db: db_dependency):
    profiles = (db.query(models_doctors.Profile)).all()
    return profiles


async def get_profile_by_id(profile_id: int, db: db_dependency):
    db_profile = db.query(models_doctors.Profile).filter(models_doctors.Profile.id == profile_id).first()

    if db_profile:
        return db_profile
    else:
        raise HTTPException(status_code=404, detail={"message": "Профиль не найден"})


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


async def service_update(service_id: int, service: ServiceUpdate, db: db_dependency):
    db_service = db.query(models_doctors.Service).filter(models_doctors.Service.id == service_id).first()

    if db_service:
        if service.name:
            db_service.name = service.name,
        if service.description:
            db_service.description = service.description
        if service.price:
            db_service.price = service.price
        if service.profile_id:
            db_service.profile_id = service.profile_id
        db.commit()
        db.refresh(db_service)
        return {"message": "Услуга успешно обновлена", "Service": db_service}

    raise HTTPException(status_code=404, detail="Услуга не найдена")


async def service_delete(service_id: int, db: db_dependency):
    db_service = db.query(models_doctors.Service).filter(models_doctors.Service.id == service_id).first()
    if db_service:
        db.delete(db_service)
        db.commit()
        return {"message": "Услуга успешно удалена", "Service": db_service}
    raise HTTPException(status_code=404, detail="Услуга не найдена")


async def get_services_by_profile_id(db: db_dependency, profile_id: int):

        services = (
            db.query
            (
                models_doctors.Service.id,
                models_doctors.Service.name,
                models_doctors.Service.description,
                models_doctors.Service.price,
                models_doctors.Profile.name.label("profile_name")
            )
            .join(models_doctors.Service, models_doctors.Service.profile_id == models_doctors.Profile.id)
        )

        if profile_id:
            services = services.filter(models_doctors.Service.profile_id == profile_id).all()

        if services:
            return [
                    {
                        "service_id": service.id,
                        "service_name": service.name,
                        "service_description": service.description,
                        "service_price": service.price,
                        "profile_name": f"{service.profile_name}"
                    }
                    for service in services
            ]
        else:
            raise HTTPException(status_code=404, detail="Услуги у профиля не найдены")


async def get_all_services(db: db_dependency):
    db_service = (
        db.query
        (
                models_doctors.Service.id,
                models_doctors.Service.name,
                models_doctors.Service.description,
                models_doctors.Service.price,
                models_doctors.Profile.name.label("profile_name")
            )
        .join(models_doctors.Service, models_doctors.Service.profile_id == models_doctors.Profile.id)
                )
    if db_service:
        return [
            {
                "service_id": service.id,
                "service_name": service.name,
                "service_description": service.description,
                "service_price": service.price,
                "profile_name": f"{service.profile_name}"
            }
            for service in db_service
        ]
    raise HTTPException(status_code=404, detail="Услуги не найдены")


async def add_experience(experience: ExperienceBase, db: db_dependency):
    db_experience = models_doctors.Experience(name=experience.name,
                                              position=experience.position,
                                              start_date=experience.start_date,
                                              end_date=experience.end_date,
                                              doctor_id=experience.doctor_id)
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    return {"message": "Опыт успешно добавлен"}


async def update_experience(experience_id: int, experience: ExperienceUpdate, db: db_dependency):

    db_experience = db.query(models_doctors.Experience).filter(models_doctors.Experience.id == experience_id).first()

    if db_experience:
        if experience.name:
            db_experience.name = experience.name,
        if experience.position:
            db_experience.position = experience.position,
        if experience.start_date:
            db_experience.start_date = experience.start_date,
        if experience.end_date:
            db_experience.end_date = experience.end_date,
        if experience.doctor_id:
            db_experience.doctor_id = experience.doctor_id
        db.commit()
        db.refresh(db_experience)
        return {"message": "Опыт успешно обновлен", "Experience": db_experience}

    raise HTTPException(status_code=404, detail="Опыт не найден")


async def delete_experience(experience_id: int, db: db_dependency):

    db_experience = db.query(models_doctors.Experience).filter(models_doctors.Experience.id == experience_id).first()
    if db_experience:
        db.delete(db_experience)
        db.commit()
        return {"message": "Опыт успешно удален"}

    raise HTTPException(status_code=404, detail="Опыт не найден")


async def get_all_experiences_by_doctor_id(doctor_id: int, db: db_dependency):

    db_doctor = db.query(models_doctors.Doctor).filter(models_doctors.Doctor.id == doctor_id).first()

    if db_doctor:
        db_experience = db.query(models_doctors.Experience).filter(models_doctors.Experience.doctor_id == doctor_id).all()

        if db_experience:
            return db_experience

        raise HTTPException(status_code=404, detail="У данного доктора не указан опыт")

    raise HTTPException(status_code=404, detail="Доктор не найден")


async def get_visits_all_for_doctor(db: db_dependency, date: str = None):
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


