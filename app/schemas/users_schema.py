from pydantic import BaseModel, EmailStr
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: EmailStr
    password: str
    is_active: Optional[bool] = False
    is_staff: Optional[bool] = False

class SignUpResponseModel(BaseModel):
    id: int
    username: Optional[str] = None
    email: EmailStr
    is_active: bool
    is_staff: bool

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
