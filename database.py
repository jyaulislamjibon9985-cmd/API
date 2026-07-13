from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load from environments.env instead of .env
load_dotenv("environments.env")

# Database URL - Use SQLite for development
DATABASE_URL = os.getenv("DATABASE_URL", None)

# Use SQLite for local development if DATABASE_URL is not set or is the default postgresql
if not DATABASE_URL or "user:password" in DATABASE_URL:
    DATABASE_URL = "sqlite:///./safety_monitoring.db"
    
# Create engine based on database type
if "sqlite" in DATABASE_URL:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    # PostgreSQL
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()