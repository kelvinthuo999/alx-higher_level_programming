#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def create_state_and_city(username, password, db_name):
    """
    Connect to the MySQL server and create the State "California"
    with the City "San Francisco" in the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.

    Returns:
        None
    """
    try:
        # Construct the MySQL connection URL
        db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, db_name)

        # Create the SQLAlchemy engine
        engine = create_engine(db_url)

        # Bind the engine to the Base class
        Base.metadata.bind = engine

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create the State "California" with the City "San Francisco"
        california = State(name="California", cities=[City(name="San Francisco")])

        # Add the State and City to the session and commit the changes
        session.add(california)
        session.commit()

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the session
        if session:
            session.close()

if __name__ == '__main__':
    """
    Connect to the database and create the State "California" with the City "San Francisco"
    using command-line arguments.
    """
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL username, password, and database name from command line arguments
    mysql_username, mysql_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to create the State and City
    create_state_and_city(mysql_username, mysql_password, db_name)
