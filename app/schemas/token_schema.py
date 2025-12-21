from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
class Token(BaseModel):
    access_token: str
    token_type: str = Field(default="bearer", example="bearer")
    expires_in: Optional[int] = Field(
        default=3600,
        description="زمان انقضا به ثانیه"
    )
    refresh_token: Optional[str] = Field(
        None,
        description="refresh access token"
    )

    class Config:
        schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer",
                "expires_in": 3600,
                "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
            }
        }


class TokenData(BaseModel):
    sub: str = Field(..., description=" (username OR email)")
    email: Optional[str] = None
    exp: Optional[datetime] = None


class TokenPayload(BaseModel):
    sub: str
    email: Optional[str] = None
