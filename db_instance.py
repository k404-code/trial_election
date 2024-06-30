# db_instance.py

from database import Database

_instance = None

def get_instance():
    global _instance
    if _instance is None:
        _instance = Database(
            dbname="postgres",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
    return _instance
