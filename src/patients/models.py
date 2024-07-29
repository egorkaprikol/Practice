from sqlalchemy import Integer, Column, String, ForeignKey, TIMESTAMP
from src.database.config import Base


class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    patronymic = Column(String)
    gender = Column(Integer, ForeignKey("genders.id"), nullable=False)
    birth_date = Column(TIMESTAMP, nullable=False)
    number = Column(String, nullable=False)
    address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


class Gender(Base):
    __tablename__ = 'genders'
    id = Column(Integer, primary_key=True)
    value = Column(String, nullable=False)


