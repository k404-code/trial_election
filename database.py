# database.py
import psycopg2

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
    
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            index INTEGER PRIMARY KEY,
            timestamp TIMESTAMP NOT NULL,
            student_id VARCHAR(50) NOT NULL,
            candidate_id VARCHAR(50) NOT NULL,
            previous_hash VARCHAR(64) NOT NULL,
            hash VARCHAR(64) NOT NULL
        );
        """)
        self.conn.commit()
        cursor.close()
    
    def insert_vote(self, vote):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO votes (index, timestamp, student_id, candidate_id, previous_hash, hash)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (vote.index, vote.timestamp, vote.student_id, vote.candidate_id, vote.previous_hash, vote.hash))
        self.conn.commit()
        cursor.close()

    def close(self):
        self.conn.close()
