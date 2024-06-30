import psycopg2

conn = psycopg2.connect(
    host="localhost", dbname="election", user="admin", password="1234", port="5432"
)

cur = conn.cursor()

def create_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS votes (
        id SERIAL PRIMARY KEY,
        index INTEGER NOT NULL,
        timestamp TIMESTAMP NOT NULL,
        student_id VARCHAR(50) NOT NULL,
        candidate_id VARCHAR(50) NOT NULL,
        previous_hash VARCHAR(64) NOT NULL,
        hash VARCHAR(64) NOT NULL);
    """)

def 

conn.commit()

cur.close()
conn.close()