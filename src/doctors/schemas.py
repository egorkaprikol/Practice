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
