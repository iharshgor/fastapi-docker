from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    is_active = Column(Boolean, default=True)
