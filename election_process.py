# election_process.py

import vote_chain as vc

def main():
    vote_chain = [vc.create_genesis_block()]
    previous_block = vote_chain[0]

    previous_block = vc.add_vote(vote_chain, previous_block, "22CA01", "Himateju")
    previous_block = vc.add_vote(vote_chain, previous_block, "5678", "Harshith")
    previous_block = vc.add_vote(vote_chain, previous_block, "9012", "Harshith")

    vote_chain[2].candidate_id = "Harshith"

    vc.print_votes(vote_chain)

if __name__ == "__main__":
    main()
