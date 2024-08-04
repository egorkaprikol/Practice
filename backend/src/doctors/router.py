from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from backend.src.auth.repository import role_required, create_user
from backend.src.database.config import db_dependency as db_dependency, get_db
from backend.src.doctors.repository import create_doctor, get_visit, create_profile, create_service, add_experience, \
    get_doctors, get_services, get_profiles
from backend.src.doctors.schemas import *

router = APIRouter()


@router.get("/secure")
async def secure(_=Depends(role_required(2))):
    return {"message": "You are authorized"}


@router.post("/doctors/register", status_code=status.HTTP_201_CREATED)
async def register(
        request: DoctorCreateRequest,
        db: Session = Depends(get_db),
        _=Depends(role_required(1)),
):
    user = create_user(db, request.login, request.password, 2)
    return await create_doctor(request, user.id, db)


@router.get("/get_visits")
async def visit_get(db: db_dependency, date: str = None):
    visits = await get_visit(db, date)
    return {"visits": visits}


@router.post("/create_profile", status_code=status.HTTP_201_CREATED)
async def profile_create(profile: ProfileCreateRequest, db: db_dependency):
    response = await create_profile(profile, db)
    return response


@router.post("/create_service", status_code=status.HTTP_201_CREATED)
async def service_create(service: ServiceCreate, db: db_dependency):
    response = await create_service(service, db)
    return response


@router.post("/add_experience", status_code=status.HTTP_201_CREATED)
async def experience_create(experience: ExperienceBase, db: db_dependency):
    response = await add_experience(experience, db)
    return response


@router.get("/get_doctors", status_code=status.HTTP_200_OK)
async def doctors_get(db: db_dependency):
    response = await get_doctors(db)
    return response


@router.get("/get_services", status_code=status.HTTP_200_OK)
async def services_get(db: db_dependency, profile_id: int):
    response = await get_services(db, profile_id)
    return response


@router.get("/get_profiles", status_code=status.HTTP_200_OK)
async def profiles_get(db: db_dependency):
    response = await get_profiles(db)
    return response

