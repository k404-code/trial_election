# vote_chain.py
import hashlib as hasher
import datetime as date
from database import Database

class VoteChain:
    def __init__(self, index, timestamp, student_id, candidate_id, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.student_id = student_id
        self.candidate_id = candidate_id
        self.previous_hash = previous_hash
        self.hash = self.hash_vote()

    def hash_vote(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.student_id).encode('utf-8') +
                   str(self.candidate_id).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

def create_genesis_block():
    return VoteChain(0, date.datetime.now(), "0", "0", "0")

def next_block(last_block, student_id, candidate_id):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_hash = last_block.hash
    return VoteChain(this_index, this_timestamp, student_id, candidate_id, this_hash)

def validate_blockchain(votechain):
    for i in range(1, len(votechain)):
        current_vote = votechain[i]
        previous_vote = votechain[i - 1]

        if current_vote.hash != current_vote.hash_vote():
            print(f"Vote {current_vote.student_id} has been tampered with.")
            return False
        
        if current_vote.previous_hash != previous_vote.hash:
            print(f"Vote {current_vote.student_id} is not linked to the previous votes correctly.")
            return False

    print("Valid blockchain")
    return True

def print_votes(votechain):
    if not validate_blockchain(votechain):
        return
    for vote in votechain:
        if vote.index != 0:  # Skip the genesis block
            print(f"Student {vote.student_id} voted for Candidate {vote.candidate_id}")

def add_vote(vote_chain, previous_block, voter_id, candidate_id, db):
    block_to_add = next_block(previous_block, voter_id, candidate_id)
    vote_chain.append(block_to_add)
    print(f"Vote added: Student {voter_id} voted for Candidate {candidate_id}")
    
    # Insert the new vote into the database
    db.insert_vote(block_to_add)
    return block_to_add
