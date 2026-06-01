from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Define where the database file will be stored on your laptop
# This will create a file named 'playersync.db' right inside your project folder!
SQLALCHEMY_DATABASE_URL = "sqlite:///./playersync.db"

# 2. Create the database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Create a Session Local class (this handles individual database operations)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create a Base class that our database tables will inherit from
Base = declarative_base()

# Helper function to get a database session and close it automatically when done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()