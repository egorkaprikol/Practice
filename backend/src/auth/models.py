from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.src.database.config import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    login: Mapped[str] = mapped_column(String(12), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(unique=True, nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False, index=True)


class Role(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(12), unique=True, index=True, nullable=False)
