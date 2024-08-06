from fastapi import APIRouter, status
from backend.src.database.config import db_dependency
from backend.src.visits.schemas import *
from backend.src.visits.repository import create_place, create_visit, update_visit, create_appointment, \
    create_review, get_reviews, get_appointments, get_appointments_by_id, get_reviews_by_id, get_visit_by_id


router = APIRouter(
    prefix=""
)


@router.post("/visits/create_visit", status_code=status.HTTP_201_CREATED)
async def visit_create(visit: VisitBase, db: db_dependency):
    response = await create_visit(visit, db)
    return response


@router.put("/visits/update/{visit_id}", status_code=status.HTTP_200_OK)
async def update_visit_route(visit_id: int, visit: VisitUpdate, db: db_dependency):
    updated_visit = await update_visit(visit_id, visit, db)
    return updated_visit


@router.get("/get_visit/{visit_id}", status_code=status.HTTP_200_OK)
async def get_visit_details(db: db_dependency, visit_id: str = None):
    response = await get_visit_by_id(db, visit_id)
    return response


@router.post("/visits/appointment/create", status_code=status.HTTP_201_CREATED)
async def appointment_create(appointment: AppointmentBase, db: db_dependency):
    response = await create_appointment(appointment, db)
    return response


@router.get("/visits/appointment/get_all", status_code=status.HTTP_200_OK)
async def appointment_get_all(db: db_dependency):
    response = await get_appointments(db)
    return response


@router.get("/visits/appointment/get_by_id", status_code=status.HTTP_200_OK)
async def appointments_get_by_id(db: db_dependency, appointment_id: int):
    response = await get_appointments_by_id(db, appointment_id)
    return response


@router.post("/reviews", status_code=status.HTTP_201_CREATED)
async def review_create(review: ReviewBase, db: db_dependency):
    response = await create_review(review, db)
    return response


@router.get("/reviews/get_all", status_code=status.HTTP_200_OK)
async def reviews_get_all(db: db_dependency):
    response = await get_reviews(db)
    return response


@router.get("/reviews/get_by_id", status_code=status.HTTP_200_OK)
async def reviews_get_by_id(db: db_dependency, review_id: int):
    response = await get_reviews_by_id(db, review_id)
    return response


@router.post("/visits/create_place", status_code=status.HTTP_201_CREATED)
async def place_create(place: PlaceBase, db: db_dependency):
    response = await create_place(place, db)
    return response
