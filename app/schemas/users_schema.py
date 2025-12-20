from pydantic import BaseModel,EmailStr
from typing import Optional

class SignUpModel(BaseModel):
    id = Optional[int]
    username: Optional[str] = None
    email: EmailStr
    password: str
    is_active: Optional[bool] = False
    is_staff: Optional[bool] = False

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "mmdsadra",
                "email": "sadrakhamesi@gmail.com",
                "password": "<PASSWORD>",
                "is_active": False,
                "is_staff": False,
            }
        }
