from datetime import datetime
from pydantic import BaseModel


class VisitBase(BaseModel):
    place_id: int
    date: datetime
    doctor_id: int
    patient_id: int
    symptom: str
    diagnosis: str
    instruction: str
    appointment_id: int


class VisitUpdate(BaseModel):
    place_id: int
    date: datetime
    doctor_id: int
    patient_id: int
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


class ReviewBase(BaseModel):
    doctor_id: int
    place_id: int
    description: str
    rate: int
    date: datetime
