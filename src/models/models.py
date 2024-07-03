from sqlalchemy import Integer, Column, String, ForeignKey
from src.database.config import Base


class Pacient(Base):
    __tablename__ = 'pacient'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    fathername = Column(String)
    gender = Column(String, ForeignKey("gender.value"), nullable=False)
    age = Column(Integer)
    sector = Column(Integer, ForeignKey("sector.number"), nullable=False)
    number = Integer
    address = Column(String)


class Gender(Base):
    __tablename__ = 'gender'
    value = Column(String, primary_key=True, nullable=False)


class Sector(Base):
    __tablename__ = 'sector'
    number = Column(Integer, primary_key=True, nullable=False)
    address = Column(String, nullable=False)

