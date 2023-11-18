#!/usr/bin/python3
"""
This script changes the name of a State object with id=2 to "New Mexico"
in the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def change_state_name(username, password, db_name):
    """
    Connect to the MySQL server and change the name of the State object with id=2 to "New Mexico".

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

        # Query the State object with id=2 and change its name to "New Mexico"
        state_to_change = session.query(State).filter_by(id=2).first()

        if state_to_change:
            state_to_change.name = "New Mexico"
            session.commit()
        else:
            print("State with id=2 not found")

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the session
        if session:
            session.close()

if __name__ == '__main__':
    """
    Connect to the database and change the name of the State object with id=2
    to "New Mexico" using command-line arguments.
    """
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL username, password, and database name from command line arguments
    mysql_username, mysql_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to change the name of the State object
    change_state_name(mysql_username, mysql_password, db_name)
