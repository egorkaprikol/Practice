from sqlalchemy import Integer, Column, String, ForeignKey, func, TIMESTAMP
from src.database.config import Base


class Visit(Base):
    __tablename__ = 'visit'
    id = Column(Integer, primary_key=True, nullable=False)
    place = Column(Integer, ForeignKey("place.id"), nullable=False)
    date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    doctor = Column(Integer, ForeignKey("doctor.id"), nullable=False)
    patient = Column(Integer, ForeignKey("patient.id"), nullable=False)
    symptom = Column(Integer, ForeignKey("symptom.id"), nullable=False)
    diagnosis = Column(Integer, ForeignKey("diagnosis.id"), nullable=False)
    instruction = Column(String, nullable=False)


class Place(Base):
    __tablename__ = 'place'
    id = Column(Integer, primary_key=True, nullable=False)
    value = Column(String, nullable=False)


class Symptom(Base):
    __tablename__ = 'symptom'
    id = Column(Integer, primary_key=True, nullable=False)
    value = Column(String, nullable=False)


class Diagnosis(Base):
    __tablename__ = 'diagnosis'
    id = Column(Integer, primary_key=True, nullable=False)
    value = Column(String, nullable=False)
