#!/usr/bin/python3
"""
This script lists all State objects containing the letter 'a' from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def list_states_with_letter_a(username, password, db_name):
    """
    Connect to the MySQL server and list all State objects containing the letter 'a' from the database.

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

        # Query and list all State objects containing the letter 'a'
        states_with_a = session.query(State).filter(State.name.contains('a')).all()

        # Display the results
        if states_with_a:
            for state in states_with_a:
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
    Connect to the database and list all State objects containing the letter 'a'
    from the database using command-line arguments.
    """
    # Check if all three arguments are provided
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <db_name>".format(argv[0]))
        exit(1)

    # Get MySQL username, password, and database name from command line arguments
    mysql_username, mysql_password, db_name = argv[1], argv[2], argv[3]

    # Call the function to list states containing the letter 'a'
    list_states_with_letter_a(mysql_username, mysql_password, db_name)
