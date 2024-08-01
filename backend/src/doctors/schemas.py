from typing import List

from pydantic import BaseModel


class DoctorBase(BaseModel):
    name: str
    surname: str
    patronymic: str
    experience: int
    phone_number: str


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


