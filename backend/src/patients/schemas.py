from datetime import date
from pydantic import BaseModel


class PatientBase(BaseModel):
    name: str
    surname: str
    patronymic: str = None
    gender_id: int
    birth_date: date
    address: str


class GenderBase(BaseModel):
    name: str
    description: str


class PatientCreateRequest(PatientBase):
    phone_number: str
    password: str

