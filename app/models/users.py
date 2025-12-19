from app.database.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey,Text
from sqlalchemy.orm import relationship
from .orders import Orders
from uuid import UUID
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(length=25,), unique=True)
    email = Column(String(length=80), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship(Orders, back_populates="users")


    def __repr__(self):
        return f"<User(id={self.id}, username={self .username}, email={self.email})>"


