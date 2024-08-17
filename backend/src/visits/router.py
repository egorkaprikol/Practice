from fastapi import APIRouter, status, Depends
from backend.src.auth.repository import role_required
from backend.src.visits.repository import *

router = APIRouter(
    prefix=""
)


@router.post("/visits", status_code=status.HTTP_201_CREATED)
async def visit_create(visit: VisitBase, db: db_dependency, _=Depends(role_required(2))):
    response = await create_visit(visit, db)
    return response


@router.put("/visits", status_code=status.HTTP_200_OK)
async def visit_update(visit_id: int, visit: VisitUpdate, db: db_dependency, _=Depends(role_required(2))):
    updated_visit = await update_visit(visit_id, visit, db)
    return updated_visit


@router.get("/visits", status_code=status.HTTP_200_OK)
async def get_visits_all(db: db_dependency):
    response = await get_all_visits(db)
    return response


@router.get("/visits/{visit_id}", status_code=status.HTTP_200_OK)
async def visit_get_by_id(db: db_dependency, visit_id):
    response = await get_visit_by_id(db, visit_id)
    return response


@router.post("/appointments", status_code=status.HTTP_201_CREATED)
async def appointment_create(appointment: AppointmentBase, db: db_dependency):
    response = await create_appointment(appointment, db)
    return response


@router.put("/appointments", status_code=status.HTTP_200_OK)
async def appointment_update(appointment_id: int, appointment: AppointmentUpdate, db: db_dependency):
    response = await update_appointment(appointment_id, appointment, db)
    return response


@router.delete("/appointments", status_code=status.HTTP_200_OK)
async def appointment_delete(appointment_id: int, db: db_dependency):
    response = await delete_appointment(appointment_id, db)
    return response


@router.get("/appointments", status_code=status.HTTP_200_OK)
async def appointment_get_all(db: db_dependency):
    response = await get_appointments_all(db)
    return response


@router.get("/appointments/{appointment_id}", status_code=status.HTTP_200_OK)
async def appointments_get_by_id(appointment_id: int, db: db_dependency):
    response = await get_appointments_by_id(appointment_id, db)
    return response


@router.post("/reviews", status_code=status.HTTP_201_CREATED)
async def review_create(review: ReviewBase, db: db_dependency):
    response = await create_review(review, db)
    return response


@router.put("/reviews", status_code=status.HTTP_200_OK)
async def review_update(review_id: int, review: ReviewUpdate, db: db_dependency):
    response = await update_review(review_id, review, db)
    return response


@router.delete("/reviews", status_code=status.HTTP_200_OK)
async def review_delete(review_id: int, db: db_dependency):
    response = await delete_review(review_id, db)
    return response


@router.get("/reviews", status_code=status.HTTP_200_OK)
async def reviews_get_all(db: db_dependency):
    response = await get_reviews_all(db)
    return response


@router.get("/reviews/{review_id}", status_code=status.HTTP_200_OK)
async def reviews_get_by_id(db: db_dependency, review_id: int):
    response = await get_reviews_by_id(db, review_id)
    return response


@router.post("/places", status_code=status.HTTP_201_CREATED)
async def place_create(place: PlaceBase, db: db_dependency, _=Depends(role_required(1))):
    response = await create_place(place, db)
    return response


@router.put("/places", status_code=status.HTTP_200_OK)
async def place_update(place_id: int, place: PlaceUpdate, db: db_dependency, _=Depends(role_required(1))):
    response = await update_place(place_id, place, db)
    return response


@router.delete("/places", status_code=status.HTTP_200_OK)
async def place_delete(place_id: int, db: db_dependency, _=Depends(role_required(1))):
    response = await delete_place(place_id, db)
    return response


@router.get("/places", status_code=status.HTTP_200_OK)
async def get_place_all(db: db_dependency):
    response = await get_all_places(db)
    return response


@router.get("/places/{place_id}", status_code=status.HTTP_200_OK)
async def place_get_by_id(place_id: int, db: db_dependency):
    response = await get_place_by_id(place_id, db)
    return response

