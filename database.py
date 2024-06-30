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

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            index INTEGER PRIMARY KEY,
            timestamp TIMESTAMP NOT NULL,
            student_id VARCHAR(50) NOT NULL,
            candidate_id INTEGER NOT NULL,
            previous_hash VARCHAR(64) NOT NULL,
            hash VARCHAR(64) NOT NULL
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            forum VARCHAR(100) NOT NULL
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

    def insert_candidate(self, name, forum):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO candidates (name, forum)
        VALUES (%s, %s)
        RETURNING id
        """, (name, forum))
        candidate_id = cursor.fetchone()[0]
        self.conn.commit()
        cursor.close()
        return candidate_id

    def remove_candidate(self, name):
        cursor = self.conn.cursor()
        cursor.execute("""
        DELETE FROM candidates
        WHERE name = %s
        """, (name,))
        self.conn.commit()
        cursor.close()

    def get_all_candidates(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM candidates")
        candidates = cursor.fetchall()
        cursor.close()
        return candidates

    def get_all_votes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM votes ORDER BY index ASC")
        votes = cursor.fetchall()
        cursor.close()
        return votes

    def close(self):
        self.conn.close()
