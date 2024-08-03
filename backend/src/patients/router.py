from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from backend.src.auth.repository import create_user
from backend.src.database.config import db_dependency, get_db
from backend.src.patients.repository import create_gender, create_patient, get_visit
from backend.src.patients.schemas import *


router = APIRouter()


@router.post("/genders/create", status_code=status.HTTP_201_CREATED)
async def gender_create(gender: GenderBase, db: db_dependency):
    response = await create_gender(gender, db)
    return response


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
        request: PatientCreateRequest,
        db: Session = Depends(get_db),
                ):
    user = create_user(db, request.login, request.password, 3)
    return await create_patient(request, user.id, db)


@router.get("/visits/get")
async def visit_get(db: db_dependency, date: str = None):
    visits = await get_visit(db, date)
    return {"visits": visits}
