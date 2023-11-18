#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_louisiana(username, password, db_name):
    """
    Connect to the MySQL server and add the State object "Louisiana" to the database.

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

        # Create the State object for "Louisiana"
        louisiana = State(name="Louisiana")

        # Add the State object to the session
        session.add(louisiana)

        # Commit the changes to the database
        session.commit()

        # Print the new states.id after creation
        print(louisiana.id)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the session
        if session:
            session.close()

if __name__ == '__main__':
    """
    Connect to the database and add the State object "Louisiana"
    to the database using command-line arguments.
    """
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL username, password, and database name from command line arguments
    mysql_username, mysql_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to add the State object "Louisiana"
    add_louisiana(mysql_username, mysql_password, db_name)
