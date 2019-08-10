#DBcm short for 'database context manager'

import mysql.connector

class UseDatabase:
    def __init__(self, config: dict) ->None:
        self.configuration = config #initialize the values passing them in a dictionary
    def __enter__(self) ->'cursor' :
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()