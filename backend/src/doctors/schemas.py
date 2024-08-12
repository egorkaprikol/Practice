from datetime import date
from pydantic import BaseModel


class DoctorBase(BaseModel):
    name: str
    surname: str
    patronymic: str = None
    birth_date: date
    gender_id: int
    profile_id: int


class DoctorUpdate(BaseModel):
    name: str
    surname: str
    patronymic: str = None
    birth_date: date
    gender_id: int
    profile_id: int


class DoctorCreateRequest(DoctorBase):
    login: str
    password: str


class ServiceCreate(BaseModel):
    name: str
    description: str = None
    price: float
    profile_id: int


class ServiceUpdate(BaseModel):
    name: str
    description: str = None
    price: float
    profile_id: int


class ProfileCreateRequest(BaseModel):
    name: str
    description: str


class ProfileUpdate(BaseModel):
    name: str
    description: str


class ExperienceBase(BaseModel):
    name: str
    position: str
    start_date: date
    end_date: date
    doctor_id: int


class ExperienceUpdate(BaseModel):
    name: str
    position: str
    start_date: date
    end_date: date
    doctor_id: int
