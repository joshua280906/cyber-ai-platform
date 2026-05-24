from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ---------------------------------------------------
# DATABASE CONFIG
# ---------------------------------------------------

DATABASE_URL = "postgresql://cyber_user:Joshua123@localhost/cyber_ai"

# ---------------------------------------------------
# SQLALCHEMY ENGINE
# ---------------------------------------------------

engine = create_engine(DATABASE_URL)

# ---------------------------------------------------
# SESSION
# ---------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ---------------------------------------------------
# BASE MODEL
# ---------------------------------------------------

Base = declarative_base()