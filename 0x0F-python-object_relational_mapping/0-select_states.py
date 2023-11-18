#!/usr/bin/python3
"""
This script lists all states from the
database specified by command-line arguments.
"""

import MySQLdb
from sys import argv

def list_states(username, password, db_name):
    """
    Connect to the MySQL server and list all states
    from the specified database.
    """
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password, db=db_name)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute the SQL query to fetch all states
        query = "SELECT * FROM states"
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

if __name__ == "__main__":
    """
    Access the database and get the states
    from the database using command-line arguments.
    """
    # Check if all three arguments are provided
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <db_name>".format(argv[0]))
        exit(1)

    # Get MySQL username, password, and database name from command line arguments
    mysql_username, mysql_password, db_name = argv[1], argv[2], argv[3]

    # Call the function to list states
    list_states(mysql_username, mysql_password, db_name)
