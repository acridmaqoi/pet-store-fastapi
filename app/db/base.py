from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:password@localhost:5432/postgres")

Session = sessionmaker(engine)

Base = declarative_base()

Base.metadata.create_all(engine)
