from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
load_dotenv()
POSTGRES_URI = os.getenv("POSTGRES_URI")
engine = create_engine(POSTGRES_URI,echo=True)