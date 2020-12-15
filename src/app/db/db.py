import os

from sqlalchemy import (Column, DateTime, Integer, Boolean,
                        String, Table, MetaData, create_engine)
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
    Column("is_adopted", Boolean()),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)