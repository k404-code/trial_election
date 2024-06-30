# election_process.py
import vote_chain as vc
from db_instance import get_instance

def main(vote_chain, voted_candidate):
    db = get_instance()
    previous_block = vote_chain[-1]  # The last block in the chain

    previous_block = vc.add_vote(vote_chain, previous_block, voted_candidate[0], voted_candidate[1], db)  # Pass db to add_vote
    vc.print_votes(vote_chain)
