from pydantic import BaseModel


class PatientBase(BaseModel):
    name: str
    surname: str
    patronymic: str
    gender: int
    age: int
    number: str
    address: str


class GenderBase(BaseModel):
    name: str
    description: str


class PatientCreateRequest(PatientBase):
    login: str
    password: str

