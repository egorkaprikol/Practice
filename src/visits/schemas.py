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


class PlaceBase(BaseModel):
    value: str

