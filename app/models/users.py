from app.database.base import Base
from sqlalchemy import Column, Integer, String, Boolean,Text,DateTime
from sqlalchemy.orm import relationship
from app.models.orders import Orders
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(length=25,), unique=True)
    email = Column(String(length=80), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship("Orders", back_populates="user")
    email_verified = Column(Boolean, default=False, nullable=False)
    email_verify_code_hash = Column(String, nullable=True)
    email_verify_expires_at = Column(DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, username={self .username}, email={self.email})>"

