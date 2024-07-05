from src.database.config import db_dependency
from src.patients import models
from src.patients.schemas import *


async def create_sector(sector: SectorBase, db: db_dependency):
    db_sector = models.Sector(number=sector.number,
                              address=sector.address)
    db.add(db_sector)
    db.commit()
    db.refresh(db_sector)
    return {"message": "Sector entry created successfully", "Sector": db_sector}


async def create_gender(gender: GenderBase, db: db_dependency):
    db_gender = models.Gender(value=gender.value)
    db.add(db_gender)
    db.commit()
    db.refresh(db_gender)
    return {"message": "Gender entry created successfully", "Sector": db_gender}
