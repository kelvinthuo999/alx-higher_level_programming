#!/usr/bin/python3
"""
This script takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

def list_cities_by_state(username, password, db_name, state_name):
    """
    Connect to the MySQL server and list all cities of a given state from the database.

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

        with connection.cursor() as cursor:
            # Execute the SQL query with parameterized query to prevent SQL injection
            query = """
                SELECT
                    cities.id, cities.name
                FROM
                    cities
                JOIN
                    states
                ON
                    cities.state_id = states.id
                WHERE
                    states.name LIKE BINARY %(state_name)s
                ORDER BY
                    cities.id ASC
            """
            cursor.execute(query, {'state_name': state_name})
            
            # Fetch all the results
            rows_selected = cursor.fetchall()

            # Display the results
            if rows_selected is not None:
                print(", ".join([row[1] for row in rows_selected]))

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close the connection
        if connection:
            connection.close()

if __name__ == "__main__":
    """
    Connect to the database and list all cities of a given state from the database
    using command-line arguments.
    """
    # Check if all four arguments are provided
    if len(argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <db_name> <state_name>".format(argv[0]))
        exit(1)

    # Get MySQL username, password, database name, and state name from command line arguments
    mysql_username, mysql_password, db_name, state_name = argv[1], argv[2], argv[3], argv[4]

    # Call the function to list cities by state
    list_cities_by_state(mysql_username, mysql_password, db_name, state_name)
