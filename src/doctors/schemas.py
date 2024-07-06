from pydantic import BaseModel


class DoctorBase(BaseModel):
    name: str
    surname: str
    father_name: str
    experience: int
    sector: int
    phone_number: str
