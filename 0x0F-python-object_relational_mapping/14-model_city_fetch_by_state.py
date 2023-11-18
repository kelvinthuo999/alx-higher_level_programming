#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def fetch_cities_by_state(username, password, db_name):
    """
    Connect to the MySQL server and fetch all City objects from the database.

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

        # Query all City objects and print the results
        cities = session.query(City).join(State).order_by(City.id).all()

        for city in cities:
            print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the session
        if session:
            session.close()

if __name__ == '__main__':
    """
    Connect to the database and fetch all City objects
    using command-line arguments.
    """
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL username, password, and database name from command line arguments
    mysql_username, mysql_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to fetch and print City objects
    fetch_cities_by_state(mysql_username, mysql_password, db_name)
