from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
load_dotenv()
POSTGRES_URI = os.getenv("POSTGRES_URI")
engine = create_engine(POSTGRES_URI,echo=True)
Session = sessionmaker(bind=engine,autoflush=False,expire_on_commit=False)
def get_database():
    db =Session()
    try:
        yield db
    finally:
        db.close()