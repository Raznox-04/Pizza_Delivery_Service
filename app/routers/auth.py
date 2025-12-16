from fastapi import APIRouter

auth_router = APIRouter(prefix="/api")

@auth_router.get("/auth")
async def root():
    return {"message": "its working"}