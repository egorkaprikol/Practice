from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.src.auth.repository import role_required, create_user
from backend.src.database.config import get_db
from backend.src.doctors.repository import *
from backend.src.doctors.schemas import *

router = APIRouter()


@router.get("/doctors/secure")
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


@router.put("/doctors/update", status_code=status.HTTP_200_OK)
async def update(doctor_id: int, doctor: DoctorUpdate, db: db_dependency):
    response = await update_doctor(doctor_id, doctor, db)
    return response


@router.delete("/doctors/delete", status_code=status.HTTP_200_OK)
async def delete(doctor_id: int, db: db_dependency):
    response = await delete_doctor(doctor_id, db)
    return response


@router.get("/doctors/get_all", status_code=status.HTTP_200_OK)
async def doctors_get(db: db_dependency):
    response = await get_doctors_all(db)
    return response


@router.get("/doctors/get_by_id", status_code=status.HTTP_200_OK)
async def doctors_get_by_id(doctor_id: int, db: db_dependency):
    response = await get_doctor_by_id(doctor_id, db)
    return response


@router.post("/profile/create", status_code=status.HTTP_201_CREATED)
async def profile_create(profile: ProfileCreateRequest, db: db_dependency):
    response = await create_profile(profile, db)
    return response


@router.put("/profile/update", status_code=status.HTTP_200_OK)
async def profile_update(profile_id: int, profile: ProfileUpdate, db: db_dependency):
    response = await update_profile(profile_id, profile, db)
    return response


@router.delete("/profile/delete", status_code=status.HTTP_200_OK)
async def profile_delete(profile_id: int, db: db_dependency):
    response = await delete_profile(profile_id, db)
    return response


@router.get("/profile/get_all", status_code=status.HTTP_200_OK)
async def profiles_get(db: db_dependency):
    response = await get_profiles_all(db)
    return response


@router.post("/create_service", status_code=status.HTTP_201_CREATED)
async def service_create(service: ServiceCreate, db: db_dependency):
    response = await create_service(service, db)
    return response


@router.get("/get_services", status_code=status.HTTP_200_OK)
async def services_get(db: db_dependency, profile_id: int):
    response = await get_services(db, profile_id)
    return response


@router.post("/add_experience", status_code=status.HTTP_201_CREATED)
async def experience_create(experience: ExperienceBase, db: db_dependency):
    response = await add_experience(experience, db)
    return response


@router.get("/get_visits")
async def visit_get(db: db_dependency, date: str = None):
    visits = await get_visits_all_for_doctor(db, date)
    return {"visits": visits}
