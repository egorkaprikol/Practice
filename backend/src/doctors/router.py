from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from backend.src.auth.repository import role_required, create_user
from backend.src.database.config import db_dependency as db_dependency, get_db
from backend.src.doctors.repository import create_doctor, get_visit, create_profile, create_service
from backend.src.doctors.schemas import *

router = APIRouter()


@router.get("/secure")
async def secure(_=Depends(role_required(2))):
    return {"message": "You are authorized"}


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
        request: DoctorCreateRequest,
        db: Session = Depends(get_db),
        _=Depends(role_required(1)),
):
    user = create_user(db, request.login, request.password, 2)
    return await create_doctor(request, user.id, db)


@router.get("/visits/get")
async def visit_get(db: db_dependency, date: str = None):
    visits = await get_visit(db, date)
    return {"visits": visits}


@router.post("/profile/create", status_code=status.HTTP_201_CREATED)
async def profile_create(profile: ProfileCreateRequest, db: db_dependency):
    response = await create_profile(profile, db)
    return response


@router.post("/service/create", status_code=status.HTTP_201_CREATED)
async def service_create(service: ServiceBase, db: db_dependency):
    response = await create_service(service, db)
    return response
