from sqlalchemy import Integer, Column, String, ForeignKey
from src.database.config import Base


class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    fathername = Column(String)
    gender = Column(Integer, ForeignKey("gender.id"), nullable=False)
    age = Column(Integer, nullable=False)
    sector = Column(Integer, ForeignKey("sector.id"), nullable=False)
    number = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    visit = Column(Integer, ForeignKey("visit.id"), nullable=False)


class Gender(Base):
    __tablename__ = 'gender'
    id = Column(Integer, primary_key=True)
    value = Column(String, nullable=False)


class Sector(Base):
    __tablename__ = 'sector'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    address = Column(String, nullable=False)