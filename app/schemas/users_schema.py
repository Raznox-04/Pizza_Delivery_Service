from pydantic import BaseModel, EmailStr
from typing import Optional
class UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = False
    is_staff: Optional[bool] = False
class SignUpModel(UserBase):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "mmdsadra",
                "email": "sadrakhamesi@gmail.com",
                "password": "securepassword123",
                "is_active": False,
                "is_staff": False,
            }
        }
class SignUpResponseModel(UserBase):
    id: int
    email: EmailStr
    username: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "username": "mmdsadra",
                "email": "sadrakhamesi@gmail.com",
                "is_active": False,
                "is_staff": False,
            }
        }
class LoginModel(BaseModel):
    email: EmailStr
    password: str

class UserUpdateModel(UserBase):
    password: Optional[str] = None