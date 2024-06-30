# election_process.py
import vote_chain as vc
from database import Database

def main(voted_candidate):
    db = Database(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    
    db.create_tables()  # Ensure the table is created if it doesn't exist
    vote_chain = [vc.create_genesis_block()]
    previous_block = vote_chain[0]

    previous_block = vc.add_vote(vote_chain, previous_block, voted_candidate[0], voted_candidate[1], db)  # Pass db to add_vote
    vc.print_votes(vote_chain)
    db.close()  # Close the database connection

if __name__ == "__main__":
    main()
