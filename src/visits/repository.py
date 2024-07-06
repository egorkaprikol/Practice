from src.database.config import db_dependency
from src.visits import models
from src.visits.schemas import PlaceBase, VisitBase


async def create_place(place: PlaceBase, db: db_dependency):
    db_place = models.Place(value=place.value)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return {"message": "Place entry created successfully", "Place": db_place}


async def create_visit(visit: VisitBase, db: db_dependency):
    db_visit = models.Visit(place=visit.place,
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
