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


def get_candidates():
    candidates = []
    num_candidates = int(input("Enter the number of candidates: "))

    for i in range(num_candidates):
        candidate_id = input("Enter the candidate ID: ")
        candidate_name = input("Enter the candidate name: ")
        candidates.append((candidate_id, candidate_name))

    return candidates

if __name__ == "__main__":
    main()