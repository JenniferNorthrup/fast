from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

# Define your database URL
db_url = "postgresql+psycopg2://username:password@localhost/mydatabase"

# Create the engine with pooling explicitly disabled
engine = create_engine(
    db_url,
    poolclass=NullPool
)