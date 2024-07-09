from fastapi import APIRouter, status
from src.database.config import db_dependency
from src.visits.schemas import *
from src.visits.repository import create_place, create_visit

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

