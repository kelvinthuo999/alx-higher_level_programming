#!/usr/bin/python3
"""
This script prints the first State object from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def print_first_state(username, password, db_name):
    """
    Connect to the MySQL server and print the first State object from the database.

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

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query and print the first State object based on states.id
        state = session.query(State).order_by(State.id).first()

        if state is not None:
            print('{0}: {1}'.format(state.id, state.name))
        else:
            print("Nothing")

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the session
        if session:
            session.close()

if __name__ == '__main__':
    """
    Connect to the database and print the first State object from the database
    using command-line arguments.
    """
    # Check if all three arguments are provided
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <db_name>".format(argv[0]))
        exit(1)

    # Get MySQL username, password, and database name from command line arguments
    mysql_username, mysql_password, db_name = argv[1], argv[2], argv[3]

    # Call the function to print the first state
    print_first_state(mysql_username, mysql_password, db_name)
