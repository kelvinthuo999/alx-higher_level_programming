#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa
where the name matches the provided argument.
"""


import MySQLdb
from sys import argv

def search_states(username, password, db_name, state_name):
    """
    Connect to the MySQL server and display all values in the states table
    where the name matches the provided argument.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): State name to search for.

    Returns:
        None
    """
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password, db=db_name)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute the SQL query with user input using format
        query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(state_name)
        cursor.execute(query)

        # Fetch all the results
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == '__main__':
    """
    Connect to the database and display all values in the states table
    where the name matches the provided argument using command-line arguments.
    """
    # Check if all four arguments are provided
    if len(argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <db_name> <state_name>".format(argv[0]))
        exit(1)

    # Get MySQL username, password, database name, and state name from command line arguments
    mysql_username, mysql_password, db_name, state_name = argv[1], argv[2], argv[3], argv[4]

    # Call the function to search and display states
    search_states(mysql_username, mysql_password, db_name, state_name)
