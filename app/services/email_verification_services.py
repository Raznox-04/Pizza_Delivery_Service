import secrets
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from fastapi import HTTPException, status
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class EmailVerificationService:
    def __init__(self, ttl_minutes: int = 10):
        self.ttl_minutes = ttl_minutes

    def generate_code(self) -> str:
        return f"{secrets.randbelow(10**6):06d}"

    def hash_code(self, code: str) -> str:
        return pwd_context.hash(code)

    def verify_code(self, code: str, hashed: str) -> bool:
        return pwd_context.verify(code, hashed)

    def now_utc(self) -> datetime:
        return datetime.now(timezone.utc)

    def expires_at(self) -> datetime:
        return self.now_utc() + timedelta(minutes=self.ttl_minutes)

    def _as_aware_utc(self, dt: datetime) -> datetime:

        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)

    def verify_and_activate(self, db, user, code: str):
        if not user.email_verify_code_hash or not user.email_verify_expires_at:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No verification code found",
            )

        expires_at = self._as_aware_utc(user.email_verify_expires_at)
        if expires_at < self.now_utc():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Verification code expired",
            )

        if not self.verify_code(code, user.email_verify_code_hash):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid code",
            )

        user.is_active = True

        if hasattr(user, "email_verified"):
            user.email_verified = True

        user.email_verify_code_hash = None
        user.email_verify_expires_at = None

        db.commit()
        db.refresh(user)
        return user
