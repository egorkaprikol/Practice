from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.auth.repository import role_required, create_user
from src.auth.schemas import SignUpRequest
from src.database.config import db_dependency as db_dependency, get_db
from src.doctors.repository import create_doctor, get_visit
from src.doctors.schemas import DoctorBase


router = APIRouter(
    prefix="/doctors"
)


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def doctor_create(doctor: DoctorBase, db: db_dependency):
    response = await create_doctor(doctor, db)
    return response


@router.get("/secure")
async def secure(_=Depends(role_required("doctor"))):
    return {"message": "You are authorized"}


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    request: SignUpRequest,
    db: Session = Depends(get_db),
    _=Depends(role_required("admin")),
):
    user = create_user(db, request.login, request.password, "doctor")
    return JSONResponse(
        {
            "message": "User created successfully. Please provide doctor information.",
            "create_doctor_url": "/doctors/create",
        }
    )


@router.get("/visits/get", status_code=status.HTTP_200_OK)
async def visit_get(db: db_dependency):
    response = await get_visit(db)
    return response
