from sqlalchemy import Integer, Column, String, ForeignKey
from src.database.config import Base


class Doctor(Base):
    __tablename__ = 'doctor'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    father_name = Column(String)
    experience = Column(Integer, nullable=False)
    sector = Column(Integer, ForeignKey("sector.id"), nullable=False)
    telephone_number = Column(Integer, nullable=False)

