# Import the necessary libraries and module
import mysql.connector
from config import HOST, USER, PASSWORD


# Exception to handle database connection errors
class DbConnectionError(Exception):
    pass


# Connecting to mysql database
def _connect_to_db(db_name):
    try:
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database=db_name
        )
        return cnx
    except mysql.connector.Error as err:
        raise DbConnectionError(f"Error: {err}")


# To close the database connection
def close_db_connection(connection):
    try:
        if connection.is_connected():
            connection.close()
            print("Database connection closed.")
    except Exception as e:
        print(f"Error while closing connection: {e}")
