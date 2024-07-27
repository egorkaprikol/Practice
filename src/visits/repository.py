from fastapi import HTTPException
from src.database.config import db_dependency
from src.visits import models as models_visits
from src.visits.schemas import PlaceBase, VisitBase, VisitUpdate


async def create_place(place: PlaceBase, db: db_dependency):
    db_place = models_visits.Place(value=place.value)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return {"message": "Place entry created successfully", "Place": db_place}


async def create_visit(visit: VisitBase, db: db_dependency):
    db_visit = models_visits.Visit(place=visit.place,
                                   date=visit.date,
                                   doctor=visit.doctor,
                                   patient=visit.patient,
                                   symptom=visit.symptom,
                                   diagnosis=visit.diagnosis,
                                   instruction=visit.instruction)
    db.add(db_visit)
    db.commit()
    db.refresh(db_visit)
    return {"message": "Patient entry created successfully", "Patient": db_visit}


async def get_visit(db: db_dependency, id: str = None):
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
