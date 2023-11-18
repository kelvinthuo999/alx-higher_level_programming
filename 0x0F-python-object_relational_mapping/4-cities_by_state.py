#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

def list_cities(username, password, db_name):
    """
    Access the database and get the cities
    from the database.

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

        with connection.cursor() as cursor:
            # Execute the SQL query to fetch all cities with state names
            query = "SELECT cities.id, cities.name, states.name \
                     FROM cities JOIN states ON cities.state_id = states.id \
                     ORDER BY cities.id ASC"
            cursor.execute(query)

            # Fetch all the results
            rows_selected = cursor.fetchall()

            # Display the results
            for row in rows_selected:
                print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close the connection
        if connection:
            connection.close()

if __name__ == '__main__':
    """
    Access the database and get the cities
    from the database using command-line arguments.
    """
    # Check if all three arguments are provided
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <db_name>".format(argv[0]))
        exit(1)

    # Get MySQL username, password, and database name from command line arguments
    mysql_username, mysql_password, db_name = argv[1], argv[2], argv[3]

    # Call the function to list cities
    list_cities(mysql_username, mysql_password, db_name)
