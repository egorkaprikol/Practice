from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class VisitBase(BaseModel):
    place: int
    date: Optional[datetime]
    doctor: int
    patient: int
    symptom: str
    diagnosis: str
    instruction: str


class VisitUpdate(BaseModel):
    place: int = None
    date: Optional[datetime]
    doctor: int = None
    patient: int = None
    symptom: str = None
    diagnosis: str = None
    instruction: str = None


class PlaceBase(BaseModel):
    value: str

