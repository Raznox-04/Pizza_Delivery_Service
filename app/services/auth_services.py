from sqlalchemy.orm import Session
from app.models.users import Users
from app.services.user_services import UserGetService
from app.schemas.users_schema import SignUpModel
from app.core.security import PasswordHasherService,pwd_context
from app.services.email_verification_services import EmailVerificationService
from app.services.email_sender import send_verification_email
class UserCreateService:
    def __init__(self, db: Session):
        self.db = db
        self.get_service = UserGetService(db)
        self.hasher = PasswordHasherService(pwd_context)
        self.email_verify = EmailVerificationService(ttl_minutes=10)

    def create_user(self, user_data : SignUpModel ) -> Users:#password should be hashed and not show plain
        if self.get_service.get_user_by_email(user_data.email) :
            raise ValueError("This Email already Registered")
        elif self.get_service.get_user_by_username(user_data.username):
            raise ValueError("This Username already Registered")
        hashed_password = self.hasher.hash_password(user_data.password)
        db_user = Users(
            username=user_data.username,
            email=user_data.email,
            password=hashed_password,
            is_active=False,
            is_staff=False,

        )
        code = self.email_verify.generate_code()
        db_user.email_verify_code_hash = self.email_verify.hash_code(code)
        db_user.email_verify_expires_at = self.email_verify.expires_at()
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        send_verification_email(db_user.email, code)
        return db_user
