# election_process.py
import vote_chain as vc
from database import Database

def main(voted_candidate):
    db = Database(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="your_db_host",
        port="your_db_port"
    )
    
    db.create_table()
    vote_chain = [vc.create_genesis_block()]
    previous_block = vote_chain[0]

    previous_block = vc.add_vote(vote_chain, previous_block, voted_candidate[0], voted_candidate[1], db)
    vc.print_votes(vote_chain)
    db.close()

if __name__ == "__main__":
    main()
