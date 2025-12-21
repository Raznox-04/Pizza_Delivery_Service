from datetime import timedelta, datetime
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, oauth2
from fastapi import HTTPException, Depends, status
from typing import Annotated, Optional
from app.models.users import Users
from app.schemas.users_schema import LoginModel
from app.schemas.token_schema import TokenPayload,TokenData
from config import settings
from passlib.context import  CryptContext
from jose import jwt,JWTError
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
class PasswordHasherService:
    def __init__(self, password_hasher: CryptContext):
        self.password_hasher = password_hasher

    def hash_password(self, password: str) -> str:
        return self.password_hasher.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.password_hasher.verify(plain_password, hashed_password)


class TokenService:
    def __init__(self):
        self.secret_key = settings.SECRET_KEY
        self.algorithm = settings.ALGORITHM
        self.access_token_time = settings.ACCESS_TOKEN_TIME
        self.refresh_token_time = settings.REFRESH_TOKEN_TIME

    def create_access_token(self, token_payload:TokenPayload,expire_time:Optional[timedelta]= None) -> str:
        to_encode = token_payload.dumps()
        if expire_time:
            expire = datetime.now() + expire_time
        else:
            expire = datetime.now() + timedelta(

                minutes=self.access_token_time
            )
        to_encode.update({"exp": expire, "type": "refresh"})
        encode_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encode_jwt

    def decode_access_token(self, token:str):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return TokenPayload(**payload)
        except JWTError:
            return None

    def verify_token(self, token:str):
        return self.decode_access_token(token) is not None
