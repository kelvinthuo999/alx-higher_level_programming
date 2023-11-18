#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_state_by_name(username, password, db_name, search_name):
    """
    Connect to the MySQL server and print the State object with the given name from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        search_name (str): State name to search.

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

        # Query and print the State object with the given name
        state = session.query(State).filter(State.name == search_name).first()

        if state is not None:
            print(state.id)
        else:
            print("Not found")

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the session
        if session:
            session.close()

if __name__ == '__main__':
    """
    Connect to the database and print the State object with the given name
    from the database using command-line arguments.
    """
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <db_name> <search_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL username, password, database name, and search name from command line arguments
    mysql_username, mysql_password, db_name, search_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Call the function to print the State object with the given name
    print_state_by_name(mysql_username, mysql_password, db_name, search_name)
