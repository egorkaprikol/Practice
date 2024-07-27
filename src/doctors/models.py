from sqlalchemy import Integer, Column, String, ForeignKey
from src.database.config import Base


class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    father_name = Column(String)
    experience = Column(Integer, nullable=False)
    sector = Column(Integer, ForeignKey("sectors.id"), nullable=False)
    phone_number = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
