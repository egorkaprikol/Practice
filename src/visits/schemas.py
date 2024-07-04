from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class VisitBase(BaseModel):
    place: int
    date: Optional[datetime]
    doctor: int
    patient: int
    symptom: int
    diagnosis: int
    instruction: str


class PlaceBase(BaseModel):
    value: str


class SymptomBase(BaseModel):
    value: str


class Diagnosis(BaseModel):
    value: str
