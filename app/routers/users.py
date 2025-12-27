from fastapi import APIRouter,Depends
from app.services.user_services import UserGetService
from app.schemas.users_schema import UserBase
from app.database.session import get_database
from sqlalchemy.orm import Session
from typing import List
user_router = APIRouter(prefix="/api", tags=["users"])
@user_router.get("/user",response_model=List[UserBase])
async def get_all_users( db: Session = Depends(get_database)):
    user_service = UserGetService(db)
    all_user = user_service.all_users()
    return all_user

@user_router.get("/user/{username}",response_model=UserBase)
async def get_user(username: str, db: Session = Depends(get_database)):
    user_service = UserGetService(db)
    useer_username=user_service.get_user_by_username(username)
    return useer_username

