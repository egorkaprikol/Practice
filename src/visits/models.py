from sqlalchemy import Integer, Column, String, ForeignKey, func, TIMESTAMP
from src.database.config import Base


class Visit(Base):
    __tablename__ = 'visit'
    id = Column(Integer, primary_key=True, nullable=False)
    place = Column(String, ForeignKey("place.id"), nullable=False)
    date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    doctor = Column(String, ForeignKey("doctor.id"), nullable=False)
    patient = Column(String, ForeignKey("patient.id"), nullable=False)
    symptom = Column(String, ForeignKey("symptom.id"), nullable=False)
    diagnosis = Column(String, ForeignKey("diagnosis.id"), nullable=False)
    instruction = Column(String, nullable=False)


class Place(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    value = Column(String, nullable=False)


class Symptom(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    value = Column(String, nullable=False)


class Diagnosis(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    value = Column(String, nullable=False)
