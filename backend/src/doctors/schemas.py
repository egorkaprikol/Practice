from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class DoctorBase(BaseModel):
    name: str
    surname: str
    patronymic: str
    birth_date: Optional[datetime]
    phone_number: str
    gender: int
    profile_id: int


class DoctorCreateRequest(DoctorBase):
    login: str
    password: str


class ServiceBase(BaseModel):
    name: str
    description: str
    price: int
    profile_id: int


class ProfileCreateRequest(BaseModel):
    name: str
    description: str


class ProfileBase(ProfileCreateRequest):
    services: List[ServiceBase] = []


class ExperienceBase(BaseModel):
    name: str
    position: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    doctor_id: int
