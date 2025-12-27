from pydantic import BaseModel, EmailStr
from typing import Optional
class UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: bool
    is_staff: bool
class SignUpModel(UserBase):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "mmdsadra",
                "email": "sadrakhamesi@gmail.com",
                "password": "sadra1383",
                "is_active": False,
                "is_staff": False,
            }
        }
class SignUpResponseModel(UserBase):
    id: int
    email: EmailStr
    username: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "mmdsadra",
                "email": "sadrakhamesi@gmail.com",
                "is_active": False,
                "is_staff": False,
            }
        }
class LoginModel(BaseModel):
    access_token: str
    token_type: str = "bearer"
    username: str
    email: EmailStr