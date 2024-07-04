from sqlalchemy import Integer, Column, String, ForeignKey
from src.database.config import Base


class Doctor(Base):
    __tablename__ = 'doctor'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    father_name = Column(String)
    experience = Column(Integer, nullable=False)
    sector = Column(Integer, ForeignKey("sector.id"), nullable=False)  # как достать сектор из другой папки чтобы он видел ключ?
    telephone_number = Column(Integer, nullable=False)
    visit = Column(Integer, ForeignKey("visit.id"), nullable=False)

