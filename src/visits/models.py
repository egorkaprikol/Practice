from sqlalchemy import Integer, Column, String, ForeignKey, func, TIMESTAMP
from src.database.config import Base


class Visit(Base):
    __tablename__ = 'visits'
    id = Column(Integer, primary_key=True, nullable=False)
    place = Column(Integer, ForeignKey("places.id"), nullable=False)
    date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    doctor = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    patient = Column(Integer, ForeignKey("patients.id"), nullable=False)
    symptom = Column(String, nullable=False)
    diagnosis = Column(String, nullable=False)
    instruction = Column(String, nullable=False)


class Place(Base):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True, nullable=False)
    value = Column(String, nullable=False)

