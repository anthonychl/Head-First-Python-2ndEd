#DBcm short for 'database context manager'
# adding exceptions

import mysql.connector

class ConnectionError(Exception):
    pass
class CredentialsError(Exception):
    pass
class SQLError(Exception):
    pass


class UseDatabase:
    def __init__(self, config: dict) ->None:
        self.configuration = config #initialize the values passing them in a dictionary
    
    def __enter__(self) ->'cursor' :
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err)
        except mysql.connector.errors.ProgrammingError as err: # if there's an incorrect user name or password
            raise CredentialsError(err)

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close() 
        # code must be added after the three lines above to ensure they execute
        if exc_trace is mysql.connector.ProgrammingError: # if there's an error with the SQL query
            raise SQLError(exc_value)
        elif exc_type: # catch any other error
            raise exc_type(exc_value)