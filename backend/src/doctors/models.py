from sqlalchemy import Integer, Column, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from backend.src.database.config import Base


class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    patronymic = Column(String)
    birth_date = Column(TIMESTAMP, nullable=False)
    gender = Column(Integer, ForeignKey("genders.id"), nullable=False)
    profile_id = Column(Integer, ForeignKey("profiles.id"), nullable=False)
    phone_number = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    services = relationship("Service", backref="profile")


class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    profile_id = Column(Integer, ForeignKey("profiles.id"), nullable=False)


class Experience(Base):
    __tablename__ = 'experiences'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    start_date = Column(TIMESTAMP, nullable=False)
    end_date = Column(TIMESTAMP, nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)


