from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.auth.repository import role_required, create_user
from src.database.config import db_dependency as db_dependency, get_db
from src.doctors.repository import create_doctor, get_visit
from src.doctors.schemas import DoctorCreateRequest

router = APIRouter(
    prefix="/doctors"
)


@router.get("/secure")
async def secure(_=Depends(role_required("doctor"))):
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
