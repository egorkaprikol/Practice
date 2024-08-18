from fastapi import HTTPException
from backend.src.database.config import db_dependency
from backend.src.patients import models as models_patients
from backend.src.patients.schemas import *
from backend.src.auth import models as models_auth


async def create_patient(patient: PatientBase, user_id, db: db_dependency):
    db_patient = models_patients.Patient(name=patient.name,
                                         surname=patient.surname,
                                         patronymic=patient.patronymic,
                                         gender_id=patient.gender_id,
                                         birth_date=patient.birth_date,
                                         address=patient.address,
                                         user_id=user_id)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return {"message": "Patient entry created successfully", "Patient": db_patient}


async def update_patient(patient_id: int, patient: PatientUpdate, db: db_dependency):
    db_patient = db.query(models_patients.Patient).filter(models_patients.Patient.id == patient_id).first()

    if db_patient:

        if patient.name:
            db_patient.name = patient.name
        if patient.surname:
            db_patient.surname = patient.surname
        if patient.patronymic:
            db_patient.patronymic = patient.patronymic
        if patient.birth_date:
            db_patient.birth_date = patient.birth_date
        if patient.gender_id:
            db_patient.gender_id = patient.gender_id
        if patient.address:
            db_patient.address = patient.address
        db.commit()
        db.refresh(db_patient)

        return {"message": "Профиль пациента успешно обновлен", "Patient": db_patient}
    else:
        raise HTTPException(status_code=404, detail="Пациент не найден")


async def delete_patient(patient_id: int, db: db_dependency):

    db_patient = db.query(models_patients.Patient).filter(models_patients.Patient.id == patient_id).first()

    if db_patient:

        ## Если удалить пациента, то вместе с ним удалится юзер в таблице users, в котором лежат логин и пароль
        user = db.query(models_auth.User).filter(
            models_auth.User.id == db_patient.user_id).first()
        db.delete(user)

        db.delete(db_patient)
        db.commit()
        return {"message": "Профиль пациента успешно удален"}
    else:
        raise HTTPException(status_code=404, detail="Пациент не найден")


async def get_all_patients(db: db_dependency):
    patient = (
        db.query(
            models_patients.Patient.id,
            models_patients.Patient.name,
            models_patients.Patient.surname,
            models_patients.Patient.patronymic,
            models_auth.User.phone_number,
        )
        .join(models_patients.Patient, models_auth.User.id == models_patients.Patient.user_id)
    )
    return [
        {
            "id": patient.id,
            "name": patient.name,
            "surname": patient.surname,
            "patronymic": patient.patronymic,
            "phone_number": patient.phone_number
        }
        for patient in patient.all()
    ]


async def get_patient_by_id(patient_id: int, db: db_dependency):

    db_patient = (
        db.query(
            models_patients.Patient.id,
            models_patients.Patient.name.label("patient_name"),
            models_patients.Patient.surname,
            models_patients.Patient.patronymic,
            models_patients.Patient.birth_date,
            models_patients.Patient.address,
            models_patients.Gender.name.label("gender_name"),
            models_auth.User.phone_number.label("patient_phone_number")
        )
        .join(models_patients.Gender, models_patients.Gender.id == models_patients.Patient.gender_id)
        .join(models_auth.User, models_auth.User.id == models_patients.Patient.user_id)
    )

    if patient_id:
        db_patient = db_patient.filter(models_patients.Patient.id == patient_id).all()

    if db_patient:
        return [
            {
                "id": patient.id,
                "name": patient.patient_name,
                "surname": patient.surname,
                "patronymic": patient.patronymic,
                "birth_date": patient.birth_date,
                "address": patient.address,
                "gender": patient.gender_name,
                "phone_number": patient.patient_phone_number
            }
            for patient in db_patient
        ]
    else:
        raise HTTPException(status_code=404, detail={"message": "Пациент не найден"})


async def create_gender(gender: GenderBase, db: db_dependency):
    db_gender = models_patients.Gender(name=gender.name,
                                       description=gender.description)
    db.add(db_gender)
    db.commit()
    db.refresh(db_gender)
    return {"message": "Gender entry created successfully", "Gender": db_gender}


async def get_all_genders(db: db_dependency):
    db_genders = db.query(models_patients.Gender).all()
    return db_genders





