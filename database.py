import pymysql
from pymysql import MySQLError
from pymysql.cursors import DictCursor
class Database:
    def __init__(self, host, user, password, database):
        self.connection = None
        try:
            # Establish the database connection using pymysql
            self.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            # Check if connection was successful by attempting a simple query
            if self.connection:
                print(f"Successfully connected to the database: {database}")
        except MySQLError as e:
            print(f"Error: {e}")
            self.connection = None

    def cursor(self):
        """Returns a cursor for executing SQL queries."""
        if not self.connection:
            print("No database connection available.")
            return None
        return self.connection.cursor(DictCursor)

    def execute_query(self, query, params=None):
        if not self.connection:
            print("No database connection available.")
            return

        try:
            with self.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
        except MySQLError as e:
            print(f"Database Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def fetch_one(self, query, params=None):
        if not self.connection:
            print("No database connection available.")
            return None

        try:
            with self.cursor() as cursor:  # Use DictCursor for dictionary result
                cursor.execute(query, params)
                return cursor.fetchone()  # Fetch one result as a dictionary
        except pymysql.MySQLError as e:
            print(f"Database Error: {e}")
            return None
        
    def fetch_all(self, query, params=None):  # Added fetch_all method
        if not self.connection:
            print("No database connection available.")
            return None

        try:
            with self.connection.cursor(DictCursor) as cursor:  # Use DictCursor
                cursor.execute(query, params)
                return cursor.fetchall()  # Fetch all results as a list of dictionaries
        except pymysql.MySQLError as e:
            print(f"Database Error: {e}")
            return None

    def close_connection(self):
        if self.connection:
            try:
                self.connection.close()
                print("Connection closed.")
            except MySQLError as e:
                print(f"Error closing connection: {e}")
