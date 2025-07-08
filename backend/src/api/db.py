import os

import sqlmodel
from sqlmodel import Session,SQLModel

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise NotImplementedError("'DATABASE_URL' needs to be set.")

# Ensure the URL uses the correct dialect for psycopg2
if DATABASE_URL.startswith("postgresql://") and "+psycopg2" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://", 1)

engine = sqlmodel.create_engine(DATABASE_URL)

def init_db():
    print("creating database tables...")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session