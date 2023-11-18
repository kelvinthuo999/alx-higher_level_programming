#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

def list_states_with_n(username, password, db_name):
    """
    Access the database and get the states
    from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.

    Returns:
        None
    """
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password, db=db_name)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute the SQL query to fetch states with names starting with 'N'
        query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC"
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
    Access the database and get the states
    from the specified database using command-line arguments.
    """
    # Check if all three arguments are provided
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <db_name>".format(argv[0]))
        exit(1)

    # Get MySQL username, password, and database name from command line arguments
    mysql_username, mysql_password, db_name = argv[1], argv[2], argv[3]

    # Call the function to list states with names starting with 'N'
    list_states_with_n(mysql_username, mysql_password, db_name)
