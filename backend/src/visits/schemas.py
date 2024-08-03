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


class AppointmentBase(BaseModel):
    date: datetime
    doctor_id: int
    place_id: int
    patient_id: int
    service_id: int
