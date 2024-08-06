from fastapi import HTTPException
from backend.src.database.config import db_dependency
from backend.src.visits import models as models_visits
from backend.src.visits.schemas import PlaceBase, VisitBase, VisitUpdate, AppointmentBase, ReviewBase


async def create_visit(visit: VisitBase, db: db_dependency):
    db_visit = models_visits.Visit(place_id=visit.place,
                                   date=visit.date,
                                   doctor_id=visit.doctor,
                                   patient_id=visit.patient,
                                   symptom=visit.symptom,
                                   diagnosis=visit.diagnosis,
                                   instruction=visit.instruction,
                                   appointment_id=visit.appointment_id)
    db.add(db_visit)
    db.commit()
    db.refresh(db_visit)
    return {"message": "Patient entry created successfully", "Patient": db_visit}


async def update_visit(visit_id: int, visit: VisitUpdate, db: db_dependency):
    db_visit = (
        db.query(models_visits.Visit)
        .filter(models_visits.Visit.id == visit_id)
        .first()
    )
    if db_visit:
        if visit.place:
            db_visit.place = visit.place
        if visit.date:
            db_visit.date = visit.date
        if visit.doctor:
            db_visit.doctor = visit.doctor
        if visit.patient:
            db_visit.patient = visit.patient
        if visit.symptom:
            db_visit.symptom = visit.symptom
        if visit.diagnosis:
            db_visit.diagnosis = visit.diagnosis
        if visit.instruction:
            db_visit.instruction = visit.instruction

        db.commit()
        db.refresh(db_visit)
        return {"message": "Осмотр успешно обновлен", "Visit": db_visit}
    else:
        raise HTTPException(status_code=404, detail="Осмотр не найден")


async def get_visit_by_id(db: db_dependency, id: int = None):
    visits = (
        db.query(
            models_visits.Visit
        )
    )

    if id:
        visits = visits.filter(models_visits.Visit.id == id)

    return [
        visit.__dict__
        for visit in visits.all()
    ]


async def create_place(place: PlaceBase, db: db_dependency):
    db_place = models_visits.Place(name=place.name,
                                   address=place.address)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return {"message": "Place entry created successfully", "Place": db_place}


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


async def get_appointments(db: db_dependency):
    appointments = (db.query(models_visits.Appointment).all())
    return appointments


async def get_appointments_by_id(db: db_dependency, appointment_id: int):
    appointments = (db.query(models_visits.Appointment).filter(models_visits.Appointment.id == appointment_id).all())
    return appointments


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


async def get_reviews(db: db_dependency):
    reviews = (db.query(models_visits.Review).all())
    return reviews


async def get_reviews_by_id(db: db_dependency, review_id: int):
    reviews = (db.query(models_visits.Review).filter(models_visits.Review.id == review_id).all())
    return reviews

