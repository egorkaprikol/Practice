from fastapi._compat import PYDANTIC_V2
from pydantic import BaseModel
from pydantic import ConfigDict


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

    if PYDANTIC_V2:  # pragma: no cover
        model_config = ConfigDict(from_attributes=True)  # type: ignore
    else:  # pragma: no cover

        class Config:
            orm_mode = True
