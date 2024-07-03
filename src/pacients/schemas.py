from pydantic import BaseModel


class PatientBase(BaseModel):
    id: int
    name: str
    surname: str
    fathername: str
    gender: str
    age: int
    sector: int
    number: int
    address: str


class GenderBase(BaseModel):
    value: str


class SectorBase(BaseModel):
    number: int
    address: str
