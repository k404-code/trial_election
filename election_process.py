# election_process.py

import vote_chain as vc


def main(voted_candidate):
    vote_chain = [vc.create_genesis_block()]
    previous_block = vote_chain[0]

    previous_block = vc.add_vote(vote_chain, previous_block, voted_candidate[0], voted_candidate[1])
    vc.print_votes(vote_chain)


if __name__ == "__main__":
    main()