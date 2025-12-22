from fastapi import APIRouter
user_router = APIRouter(prefix="/users", tags=["users"])
@user_router.get("/user")
async def get_user():
    pass