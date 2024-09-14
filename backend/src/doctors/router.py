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


@router.post("/doctors", status_code=status.HTTP_201_CREATED)
async def register(
        request: DoctorCreateRequest,
        db: Session = Depends(get_db),
        _=Depends(role_required(1)),):
    user = create_user(db, request.phone_number, request.password, 2)
    return await create_doctor(request, user.id, db)


@router.patch("/doctors", status_code=status.HTTP_200_OK)
async def update(doctor_id: int, doctor: DoctorUpdate, db: db_dependency, _=Depends(role_required(1)),):
    response = await update_doctor(doctor_id, doctor, db)
    return response


@router.delete("/doctors", status_code=status.HTTP_200_OK)
async def delete(doctor_id: int, db: db_dependency, _=Depends(role_required(1)),):
    response = await delete_doctor(doctor_id, db)
    return response


@router.get("/doctors", status_code=status.HTTP_200_OK)
async def doctors_get(db: db_dependency):
    response = await get_doctors_all(db)
    return response


@router.get("/doctors/{doctor_id}", status_code=status.HTTP_200_OK)
async def doctors_get_by_id(doctor_id: int, db: db_dependency):
    response = await get_doctor_by_id(doctor_id, db)
    return response


@router.post("/profiles", status_code=status.HTTP_201_CREATED)
async def profile_create(profile: ProfileCreateRequest, db: db_dependency):
    response = await create_profile(profile, db)
    return response


@router.put("/profiles", status_code=status.HTTP_200_OK)
async def profile_update(profile_id: int, profile: ProfileUpdate, db: db_dependency):
    response = await update_profile(profile_id, profile, db)
    return response


@router.delete("/profiles", status_code=status.HTTP_200_OK)
async def profile_delete(profile_id: int, db: db_dependency):
    response = await delete_profile(profile_id, db)
    return response


@router.get("/profiles", status_code=status.HTTP_200_OK)
async def profiles_get(db: db_dependency):
    response = await get_profiles_all(db)
    return response


@router.get("/profiles/{profile_id}", status_code=status.HTTP_200_OK)
async def get_profiles_by_id(profile_id: int, db: db_dependency):
    response = await get_profile_by_id(profile_id, db)
    return response


@router.post("/services", status_code=status.HTTP_201_CREATED)
async def service_create(service: ServiceCreate, db: db_dependency):
    response = await create_service(service, db)
    return response


@router.put("/services", status_code=status.HTTP_200_OK)
async def update_service(service_id: int, service: ServiceUpdate, db: db_dependency):
    response = await service_update(service_id, service, db)
    return response


@router.delete("/services", status_code=status.HTTP_200_OK)
async def delete_service(service_id: int, db: db_dependency):
    response = await service_delete(service_id, db)
    return response


@router.get("/services/{profile_id}", status_code=status.HTTP_200_OK)
async def services_get(db: db_dependency, profile_id: int):
    response = await get_services_by_profile_id(db, profile_id)
    return response


@router.get("/services", status_code=status.HTTP_200_OK)
async def get_services(db: db_dependency):
    response = await get_all_services(db)
    return response


@router.post("/experiences", status_code=status.HTTP_201_CREATED)
async def experience_create(experiences: List[ExperienceBase], db: db_dependency):
    response = await add_experience(experiences, db)
    return response


@router.put("/experiences", status_code=status.HTTP_200_OK)
async def experience_update(experience_id: int, experiences: List[ExperienceUpdate], db: db_dependency):
    response = await update_experience(experience_id, experiences, db)
    return response


@router.delete("/experiences", status_code=status.HTTP_200_OK)
async def experience_delete(experience_id: int, db: db_dependency):
    response = await delete_experience(experience_id, db)
    return response


@router.delete("/experiences/doctor_id={doctor_id}", status_code=status.HTTP_200_OK)
async def delete_experience_by_doctor(doctor_id: int, db: db_dependency):
    response = await delete_experience_by_doctor_id(doctor_id, db)
    return response


@router.get("/experiences/{experience_id}", status_code=status.HTTP_200_OK)
async def experience_get_by_id(experience_id: int, db: db_dependency):
    response = await get_experience_by_id(experience_id, db)
    return response


@router.get("/experiences/get_by_doctor_id/{doctor_id}", status_code=status.HTTP_200_OK)
async def experience_get_all_by_doctor_id(doctor_id: int, db: db_dependency):
    response = await get_all_experiences_by_doctor_id(doctor_id, db)
    return response

