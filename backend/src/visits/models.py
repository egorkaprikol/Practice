from datetime import datetime
from sqlalchemy import String, ForeignKey, func, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from backend.src.database.config import Base


class Visit(Base):
    __tablename__ = 'visits'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    date: Mapped[datetime] = mapped_column(insert_default=func.now(), index=True)
    symptom: Mapped[str] = mapped_column(String(128), nullable=False)
    diagnosis: Mapped[str] = mapped_column(String(64), nullable=False)
    instruction: Mapped[str] = mapped_column(String(256), nullable=False)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"), nullable=False, index=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"), nullable=False, index=True)
    place_id: Mapped[int] = mapped_column(ForeignKey("places.id"), nullable=False, index=True)
    appointment_id: Mapped[int] = mapped_column(ForeignKey("appointments.id"), nullable=False, index=True)


class Place(Base):
    __tablename__ = 'places'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    address: Mapped[str] = mapped_column(String(128), nullable=False, index=True)


class Appointment(Base):
    __tablename__ = 'appointments'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    date: Mapped[datetime] = mapped_column(insert_default=func.now(), index=True)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"), nullable=False, index=True)
    place_id: Mapped[int] = mapped_column(ForeignKey("places.id"), nullable=False, index=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"), nullable=False, index=True)
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"), nullable=False, index=True)


class Review(Base):
    __tablename__ = 'reviews'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    description: Mapped[str] = mapped_column(String(256), nullable=True)
    rate: Mapped[int] = mapped_column(nullable=False, index=True)
    date: Mapped[datetime] = mapped_column(insert_default=func.now())
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"), nullable=False, index=True)
    place_id: Mapped[int] = mapped_column(ForeignKey("places.id"), nullable=False, index=True)

    __table_args__ = (
        CheckConstraint('rate BETWEEN 0 AND 5', name='rate_check'),
    )
