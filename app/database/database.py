from dotenv import load_dotenv
from sqlalchemy import create_engine
from session import Session
import os
load_dotenv()
POSTGRES_URI = os.getenv("POSTGRES_URI")
engine = create_engine(POSTGRES_URI,echo=True)

def get_database():
    db =Session()
    try:
        yield db
    finally:
        db.close()