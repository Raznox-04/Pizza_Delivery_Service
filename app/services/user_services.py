from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.models.users import Users
class UserGetService:
    def __init__(self, db: Session):
        self.db = db
    def get_user_by_username(self, user_username: str) -> Users:
        user = self.db.query(Users).filter(Users.username == user_username).first()
        return user

    def get_user_by_email(self, user_email: EmailStr):
        user = self.db.query(Users).filter(Users.email == user_email).first()
        return user