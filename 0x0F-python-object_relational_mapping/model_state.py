#!/usr/bin/python3
"""
This script defines the State class and creates an instance of Base using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace 'mysql_user', 'mysql_password', 'database_name' with your MySQL credentials
DATABASE_URI = 'mysql+mysqldb://mysql_user:mysql_password@localhost:3306/database_name'

Base = declarative_base()

class State(Base):
    """
    State class represents the states table in MySQL.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

# Connect to the MySQL server
engine = create_engine(DATABASE_URI)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Close the session
session.close()
