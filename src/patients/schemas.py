from pydantic import BaseModel


class PatientBase(BaseModel):
    name: str
    surname: str
    father_name: str
    gender: int
    age: int
    sector: int
    number: int
    address: str


class GenderBase(BaseModel):
    value: str


class SectorBase(BaseModel):
    number: int
    address: str
