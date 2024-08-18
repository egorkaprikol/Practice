from fastapi import HTTPException
from backend.src.database.config import db_dependency
from backend.src.visits import models as models_visits
from backend.src.doctors import models as models_doctors
from backend.src.patients import models as models_patients
from backend.src.visits.schemas import *


async def create_visit(visit: VisitBase, db: db_dependency):
    db_visit = models_visits.Visit(place_id=visit.place_id,
                                   date=visit.date,
                                   doctor_id=visit.doctor_id,
                                   patient_id=visit.patient_id,
                                   symptom=visit.symptom,
                                   diagnosis=visit.diagnosis,
                                   instruction=visit.instruction,
                                   appointment_id=visit.appointment_id)
    db.add(db_visit)
    db.commit()
    db.refresh(db_visit)
    return {"message": "Осмотр успешно создан", "Осмотр": db_visit}


async def update_visit(visit_id: int, visit: VisitUpdate, db: db_dependency):

    db_visit = db.query(models_visits.Visit).filter(models_visits.Visit.id == visit_id).first()

    if db_visit:
        if visit.place_id:
            db_visit.place_id = visit.place_id
        if visit.date:
            db_visit.date = visit.date
        if visit.doctor_id:
            db_visit.doctor_id = visit.doctor_id
        if visit.patient_id:
            db_visit.patient_id = visit.patient_id
        if visit.symptom:
            db_visit.symptom = visit.symptom
        if visit.diagnosis:
            db_visit.diagnosis = visit.diagnosis
        if visit.instruction:
            db_visit.instruction = visit.instruction
        if visit.appointment_id:
            db_visit.appointment_id = visit.appointment_id

        db.commit()
        db.refresh(db_visit)
        return {"message": "Осмотр успешно обновлен", "Осмотр": db_visit}
    else:
        raise HTTPException(status_code=404, detail="Осмотр не найден")


async def get_all_visits(db: db_dependency):

    visits = (
        db.query(
            models_visits.Visit.id,
            models_visits.Visit.date,
            models_visits.Visit.symptom,
            models_visits.Visit.diagnosis,
            models_visits.Visit.instruction,
            models_doctors.Doctor.name.label("doctor_name"),
            models_doctors.Doctor.surname.label("doctor_surname"),
            models_doctors.Doctor.patronymic.label("doctor_patronymic"),
            models_patients.Patient.name.label("patient_name"),
            models_patients.Patient.surname.label("patient_surname"),
            models_patients.Patient.patronymic.label("patient_patronymic"),
            models_visits.Appointment.id.label("appointment_id"),
            models_visits.Appointment.date.label("appointment_date"),
            models_visits.Place.name.label("place_name"),
            models_visits.Place.address
        )
        .join(models_doctors.Doctor, models_doctors.Doctor.id == models_visits.Visit.doctor_id)
        .join(models_patients.Patient, models_patients.Patient.id == models_visits.Visit.patient_id)
        .join(models_visits.Appointment, models_visits.Appointment.id == models_visits.Visit.appointment_id)
        .join(models_visits.Place, models_visits.Place.id == models_visits.Visit.place_id)
    )

    if visits:
        return [
            {
                "id": visit.id,
                "date": visit.date,
                "symptom": visit.symptom,
                "diagnosis": visit.diagnosis,
                "instruction": visit.instruction,
                "doctor_name": visit.doctor_name,
                "doctor_surname": visit.doctor_surname,
                "doctor_patronymic": visit.doctor_patronymic,
                "patient_name": visit.patient_name,
                "patient_surname": visit.patient_surname,
                "patient_patronymic": visit.patient_patronymic,
                "appointment_id": visit.appointment_id,
                "appointment_date": visit.appointment_date,
                "place_name": visit.place_name,
                "place_address": visit.address
            }
            for visit in visits.all()
        ]
    else:
        raise HTTPException(status_code=404, detail="Осмотры не найдены")


async def get_visit_by_id(db: db_dependency, visit_id):

    db_visit = (
        db.query(
            models_visits.Visit.id,
            models_visits.Visit.date,
            models_visits.Visit.symptom,
            models_visits.Visit.diagnosis,
            models_visits.Visit.instruction,
            models_doctors.Doctor.name.label("doctor_name"),
            models_doctors.Doctor.surname.label("doctor_surname"),
            models_doctors.Doctor.patronymic.label("doctor_patronymic"),
            models_patients.Patient.name.label("patient_name"),
            models_patients.Patient.surname.label("patient_surname"),
            models_patients.Patient.patronymic.label("patient_patronymic"),
            models_visits.Appointment.id.label("appointment_id"),
            models_visits.Appointment.date.label("appointment_date"),
            models_visits.Place.name.label("place_name"),
            models_visits.Place.address
        )
        .join(models_doctors.Doctor, models_doctors.Doctor.id == models_visits.Visit.doctor_id)
        .join(models_patients.Patient, models_patients.Patient.id == models_visits.Visit.patient_id)
        .join(models_visits.Appointment, models_visits.Appointment.id == models_visits.Visit.appointment_id)
        .join(models_visits.Place, models_visits.Place.id == models_visits.Visit.place_id)
    )

    if visit_id:
        db_visit = db_visit.filter(models_visits.Visit.id == visit_id).all()

    if db_visit:
        return [
            {
                "id": visit.id,
                "date": visit.date,
                "symptom": visit.symptom,
                "diagnosis": visit.diagnosis,
                "instruction": visit.instruction,
                "doctor_name": visit.doctor_name,
                "doctor_surname": visit.doctor_surname,
                "doctor_patronymic": visit.doctor_patronymic,
                "patient_name": visit.patient_name,
                "patient_surname": visit.patient_surname,
                "patient_patronymic": visit.patient_patronymic,
                "appointment_id": visit.appointment_id,
                "appointment_date": visit.appointment_date,
                "place_name": visit.place_name,
                "place_address": visit.address
            }
            for visit in db_visit
                ]

    else:
        raise HTTPException(status_code=404, detail="Осмотр не найден")


async def get_visits_all_for_doctors(db: db_dependency, date: str = None):
    visits = (
        db.query(
            models_visits.Visit.date,
            models_patients.Patient.name.label("patient_name"),
            models_patients.Patient.surname.label("patient_surname"),
            models_patients.Patient.patronymic.label("patient_patronymic"),
        )
        .join(models_patients.Patient, models_visits.Visit.patient_id == models_patients.Patient.id)
    )

    if date:
        visits = visits.filter(models_visits.Visit.date == date).all()

    return [
        {
            "date": visit.date,
            "patient_name": f"{visit.patient_name} {visit.patient_surname} {visit.patient_patronymic}",
        }
        for visit in visits
    ]


async def get_visits_all_for_patients(db: db_dependency, date: str = None):
    visits = (
        db.query(
            models_visits.Visit.date,
            models_doctors.Doctor.name.label("doctor_name"),
            models_doctors.Doctor.surname.label("doctor_surname"),
            models_doctors.Doctor.patronymic.label("doctor_patronymic"),
        )
        .join(models_doctors.Doctor, models_visits.Visit.doctor_id == models_doctors.Doctor.id)
    )

    if date:
        visits = visits.filter(models_visits.Visit.date == date).all()

    return [
        {
            "date": visit.date,
            "doctor_name": f"{visit.doctor_name} {visit.doctor_surname} {visit.doctor_patronymic}",
        }
        for visit in visits
    ]


async def create_appointment(appointment: AppointmentBase, db: db_dependency):
    db_appointment = models_visits.Appointment(date=appointment.date,
                                               doctor_id=appointment.doctor_id,
                                               patient_id=appointment.patient_id,
                                               place_id=appointment.place_id,
                                               service_id=appointment.service_id)
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return {"message": "Заявка успешно создана", "Appointment": db_appointment}


async def update_appointment(appointment_id: int, appointment: AppointmentUpdate, db: db_dependency):

    db_appointment = db.query(models_visits.Appointment).filter(models_visits.Appointment.id == appointment_id).first()

    if db_appointment:
        if appointment.date:
            db_appointment.date = appointment.date,
        if appointment.doctor_id:
            db_appointment.doctor_id = appointment.doctor_id,
        if appointment.patient_id:
            db_appointment.patient_id = appointment.patient_id,
        if appointment.place_id:
            db_appointment.place_id = appointment.place_id,
        if appointment.service_id:
            db_appointment.service_id = appointment.service_id

        db.commit()
        db.refresh(db_appointment)
        return {"message": "Заявка успешно обновлена", "Appointment": db_appointment}
    else:
        raise HTTPException(status_code=404, detail="Заявка не найдена")


async def delete_appointment(appointment_id: int, db: db_dependency):

    db_appointment = db.query(models_visits.Appointment).filter(models_visits.Appointment.id == appointment_id).first()

    if db_appointment:
        db.delete(db_appointment)
        db.commit()
        return {"message": "Заявка успешно удалена"}
    else:
        raise HTTPException(status_code=404, detail="Заявка не найдена")


async def get_appointments_all(db: db_dependency):
    appointments = (
        db.query(
            models_visits.Appointment.id,
            models_visits.Appointment.date,
            models_visits.Place.name.label("place_name"),
            models_visits.Place.address,
            models_patients.Patient.name.label("patient_name"),
            models_patients.Patient.surname.label("patient_surname"),
            models_patients.Patient.patronymic.label("patient_patronymic"),
            models_doctors.Doctor.name.label("doctor_name"),
            models_doctors.Doctor.surname.label("doctor_surname"),
            models_doctors.Doctor.patronymic.label("doctor_patronymic"),
            models_doctors.Service.name.label("service_name"),
            models_doctors.Service.price,
            models_doctors.Profile.name.label("profile_name"),
        )
        .join(models_visits.Place, models_visits.Place.id == models_visits.Appointment.place_id)
        .join(models_patients.Patient, models_patients.Patient.id == models_visits.Appointment.patient_id)
        .join(models_doctors.Doctor, models_doctors.Doctor.id == models_visits.Appointment.doctor_id)
        .join(models_doctors.Service, models_doctors.Service.id == models_visits.Appointment.service_id)
        .join(models_doctors.Profile, models_doctors.Service.profile_id == models_doctors.Profile.id)
    )
    return [
            {
                "id": appointment.id,
                "date": appointment.date,
                "place_name": appointment.place_name,
                "address": appointment.address,
                "patient_name": appointment.patient_name,
                "patient_surname": appointment.patient_surname,
                "patient_patronymic": appointment.patient_patronymic,
                "doctor_name": appointment.doctor_name,
                "doctor_surname": appointment.doctor_surname,
                "doctor_patronymic": appointment.doctor_patronymic,
                "service_name": appointment.service_name,
                "service_price": appointment.price,
                "profile_name": appointment.profile_name
            }
            for appointment in appointments.all()
        ]


async def get_appointments_by_id(appointment_id: int, db: db_dependency):

    appointments = (
        db.query(
            models_visits.Appointment.id,
            models_visits.Appointment.date,
            models_visits.Place.name.label("place_name"),
            models_visits.Place.address,
            models_patients.Patient.name.label("patient_name"),
            models_patients.Patient.surname.label("patient_surname"),
            models_patients.Patient.patronymic.label("patient_patronymic"),
            models_doctors.Doctor.name.label("doctor_name"),
            models_doctors.Doctor.surname.label("doctor_surname"),
            models_doctors.Doctor.patronymic.label("doctor_patronymic"),
            models_doctors.Service.name.label("service_name"),
            models_doctors.Service.price,
            models_doctors.Profile.name.label("profile_name"),
        )
        .join(models_visits.Place, models_visits.Place.id == models_visits.Appointment.place_id)
        .join(models_patients.Patient, models_patients.Patient.id == models_visits.Appointment.patient_id)
        .join(models_doctors.Doctor, models_doctors.Doctor.id == models_visits.Appointment.doctor_id)
        .join(models_doctors.Service, models_doctors.Service.id == models_visits.Appointment.service_id)
        .join(models_doctors.Profile, models_doctors.Service.profile_id == models_doctors.Profile.id)
    )

    if appointment_id:
        appointments = appointments.filter(models_visits.Appointment.id == appointment_id).all()

    if appointments:

        return [
            {
                "id": appointment.id,
                "date": appointment.date,
                "place_name": appointment.place_name,
                "address": appointment.address,
                "patient_name": appointment.patient_name,
                "patient_surname": appointment.patient_surname,
                "patient_patronymic": appointment.patient_patronymic,
                "doctor_name": appointment.doctor_name,
                "doctor_surname": appointment.doctor_surname,
                "doctor_patronymic": appointment.doctor_patronymic,
                "service_name": appointment.service_name,
                "service_price": appointment.price,
                "profile_name": appointment.profile_name
            }
            for appointment in appointments
        ]
    else:
        raise HTTPException(status_code=404, detail="Заявка не найдена")


async def create_review(review: ReviewBase, db: db_dependency):
    db_review = models_visits.Review(date=review.date,
                                     doctor_id=review.doctor_id,
                                     place_id=review.place_id,
                                     description=review.description,
                                     rate=review.rate)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return {"message": "Спасибо за обратную связь!", "Ваш отзыв:": db_review}


async def update_review(review_id: int, review: ReviewUpdate, db: db_dependency):

    db_review = db.query(models_visits.Review).filter(models_visits.Review.id == review_id).first()

    if db_review:

        if review.date:
            db_review.date = review.date
        if review.doctor_id:
            db_review.doctor_id = review.doctor_id
        if review.place_id:
            db_review.place_id = review.place_id
        if review.description:
            db_review.description = review.description
        if review.rate:
            db_review.rate = review.rate
        db.commit()
        db.refresh(db_review)

        return {"message": "Отзыв успешно обновлен", "Review": db_review}
    else:
        raise HTTPException(status_code=404, detail="Отзыв не найден")


async def delete_review(review_id: int, db: db_dependency):

    db_review = db.query(models_visits.Review).filter(models_visits.Review.id == review_id).first()

    if db_review:
        db.delete(db_review)
        db.commit()
        return {"message": "Отзыв успешно удален"}
    else:
        raise HTTPException(status_code=404, detail="Отзыв не найден")


async def get_reviews_all(db: db_dependency):

    db_review = (
        db.query(
            models_visits.Review.id,
            models_visits.Review.rate,
            models_visits.Review.description,
            models_visits.Review.date,
            models_doctors.Doctor.name,
            models_doctors.Doctor.surname,
            models_doctors.Doctor.patronymic,
            models_visits.Place.name.label("place_name"),
            models_visits.Place.address
        )
        .join(models_doctors.Doctor, models_doctors.Doctor.id == models_visits.Review.doctor_id)
        .join(models_visits.Place, models_visits.Place.id == models_visits.Review.place_id)
    )

    if db_review:

        return [
            {
                "id": review.id,
                "rate": review.rate,
                "description": review.description,
                "date": review.date,
                "doctor_name": review.name,
                "doctor_surname": review.surname,
                "doctor_patronymic": review.patronymic,
                "place_name": review.place_name,
                "address": review.address
            }
            for review in db_review.all()
        ]
    else:
        raise HTTPException(status_code=404, detail="Отзывы не найден")


async def get_reviews_by_id(db: db_dependency, review_id: int):

    db_review = (
        db.query(
            models_visits.Review.id,
            models_visits.Review.rate,
            models_visits.Review.description,
            models_visits.Review.date,
            models_doctors.Doctor.name,
            models_doctors.Doctor.surname,
            models_doctors.Doctor.patronymic,
            models_visits.Place.name.label("place_name"),
            models_visits.Place.address
        )
        .join(models_doctors.Doctor, models_doctors.Doctor.id == models_visits.Review.doctor_id)
        .join(models_visits.Place, models_visits.Place.id == models_visits.Review.place_id)
    )

    if review_id:

        db_review = db_review.filter(models_visits.Review.id == review_id).all()

    if db_review:

        return [
            {
                "id": review.id,
                "rate": review.rate,
                "description": review.description,
                "date": review.date,
                "doctor_name": review.name,
                "doctor_surname": review.surname,
                "doctor_patronymic": review.patronymic,
                "place_name": review.place_name,
                "address": review.address
            }
            for review in db_review
        ]
    else:
        raise HTTPException(status_code=404, detail="Отзыв не найден")


async def create_place(place: PlaceBase, db: db_dependency):
    db_place = models_visits.Place(name=place.name,
                                   address=place.address)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return {"message": "Place entry created successfully", "Place": db_place}


async def update_place(place_id: int, place: PlaceUpdate, db: db_dependency):

    db_place = db.query(models_visits.Place).filter(models_visits.Place.id == place_id).first()

    if db_place:
        if place.name:
            db_place.name = place.name,
        if place.address:
            db_place.address = place.address
        db.commit()
        db.refresh(db_place)
        return {"message": "Место успешно обновлено", "Place": db_place}
    else:
        raise HTTPException(status_code=404, detail="Место не найдено")


async def delete_place(place_id: int, db: db_dependency):

    db_place = db.query(models_visits.Place).filter(models_visits.Place.id == place_id).first()

    if db_place:
        db.delete(db_place)
        db.commit()
        return {"message": "Место успешно удалено"}
    else:
        raise HTTPException(status_code=404, detail="Место не найдено")


async def get_all_places(db: db_dependency):

    db_place = db.query(models_visits.Place).all()
    if db_place:
        return db_place
    else:
        raise HTTPException(status_code=404, detail="Места не найдены")


async def get_place_by_id(place_id: int, db: db_dependency):

    db_place = db.query(models_visits.Place).filter(models_visits.Place.id == place_id).first()

    if db_place:
        return db_place
    else:
        raise HTTPException(status_code=404, detail="Место не найдено")
