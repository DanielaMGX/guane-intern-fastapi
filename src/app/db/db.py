import os

from sqlalchemy import (Column, DateTime, Integer, Boolean,
                        String, Table, MetaData, create_engine,ForeignKey)
from sqlalchemy.sql import func
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
dog = Table(
    "dog",
    metadata,
    Column("id", String(), primary_key=True),
    Column("name", String(), unique=True),
    Column("picture", String()),
    Column("is_adopted", Boolean(), default=False),
    Column("created_date", DateTime, default=func.now(), nullable=False),
    Column("user_id", Integer, ForeignKey("user.id"), nullable=True)

)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String()),
    Column("last_name", String()),
    Column("email", String()),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)
# databases query builder
database = Database(DATABASE_URL)