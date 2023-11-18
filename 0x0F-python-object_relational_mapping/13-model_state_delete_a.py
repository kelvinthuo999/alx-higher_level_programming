#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def delete_states_with_letter_a(username, password, db_name):
    """
    Connect to the MySQL server and delete all State objects with a name containing the letter 'a'
    from the database.

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

        # Query and delete all State objects with a name containing the letter 'a'
        states_with_a = session.query(State).filter(State.name.ilike('%a%')).all()

        for state in states_with_a:
            session.delete(state)

        # Commit the changes to the database
        session.commit()

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the session
        if session:
            session.close()

if __name__ == '__main__':
    """
    Connect to the database and delete all State objects with a name containing the letter 'a'
    using command-line arguments.
    """
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL username, password, and database name from command line arguments
    mysql_username, mysql_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to delete states with a name containing the letter 'a'
    delete_states_with_letter_a(mysql_username, mysql_password, db_name)
