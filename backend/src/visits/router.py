from fastapi import APIRouter, status
from backend.src.database.config import db_dependency
from backend.src.visits.schemas import *
from backend.src.visits.repository import create_place, create_visit, get_visit, update_visit

router = APIRouter(
    prefix="/visits"
)


@router.post("/place/create", status_code=status.HTTP_201_CREATED)
async def place_create(place: PlaceBase, db: db_dependency):
    response = await create_place(place, db)
    return response


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def visit_create(visit: VisitBase, db: db_dependency):
    response = await create_visit(visit, db)
    return response


@router.get("/{visit_id}")
async def get_visit_details(db: db_dependency, visit_id: str = None):
    response = await get_visit(db, visit_id)
    return response


@router.put("/update/{visit_id}")
async def update_visit_route(visit_id: int, visit: VisitUpdate, db: db_dependency):
    updated_visit = await update_visit(visit_id, visit, db)
    return updated_visit
