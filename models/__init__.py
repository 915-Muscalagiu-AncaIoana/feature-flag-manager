# This file is required for Alembic migrations
from models.database import engine
from models.feature_flag import Base

Base.metadata.create_all(bind=engine)
