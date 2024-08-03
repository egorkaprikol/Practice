from datetime import date
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.src.database.config import Base


class Patient(Base):
    __tablename__ = 'patients'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    surname: Mapped[str] = mapped_column(String(30), nullable=False)
    patronymic: Mapped[str] = mapped_column(String(30), nullable=True)
    gender: Mapped[int] = mapped_column(ForeignKey("genders.id"), nullable=False)
    birth_date: Mapped[date] = mapped_column(nullable=False, index=True)
    phone_number: Mapped[str] = mapped_column(String(12), nullable=False, index=True, unique=True)
    address: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)


class Gender(Base):
    __tablename__ = 'genders'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(16), nullable=False, unique=True, index=True)
    description: Mapped[str] = mapped_column(String(50), nullable=False)


