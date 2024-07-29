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
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False)


class Place(Base):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)


class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True, nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    place_id = Column(Integer, ForeignKey("places.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)


class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    place_id = Column(Integer, ForeignKey("places.id"), nullable=False)
    description = Column(String, nullable=False)
    rate = Column(Integer, nullable=False)
    date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
