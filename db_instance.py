# db_instance.py

from database import Database

_instance = None

def get_instance():
    global _instance
    if _instance is None:
        _instance = Database(
            dbname="test",
            user="postgres",
            password="goat1825",
            host="localhost",
            port="5432"
        )
    return _instance
