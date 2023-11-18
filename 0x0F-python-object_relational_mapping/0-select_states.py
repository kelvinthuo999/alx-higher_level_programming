#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, db_name):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute the SQL query to fetch all states sorted by states.id
        query = "SELECT * FROM states ORDER BY states.id"
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
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL username, password, and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Call the function to list states
    list_states(mysql_username, mysql_password, db_name)
