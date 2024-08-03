from datetime import datetime
from pydantic import BaseModel


class VisitBase(BaseModel):
    place: int
    date: datetime
    doctor: int
    patient: int
    symptom: str
    diagnosis: str
    instruction: str
    appointment_id: int


class VisitUpdate(BaseModel):
    place: int
    date: datetime
    doctor: int
    patient: int
    symptom: str
    diagnosis: str
    instruction: str
    appointment_id: int


class PlaceBase(BaseModel):
    name: str
    address: str

