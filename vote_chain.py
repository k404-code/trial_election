# vote_chain.py

import hashlib
import datetime as date
from db_instance import get_instance

class VoteBlock:
    def __init__(self, index, timestamp, student_id, candidate_id, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.student_id = student_id
        self.candidate_id = candidate_id
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        vote_data = f'{self.index}{self.timestamp}{self.student_id}{self.candidate_id}{self.previous_hash}'
        return hashlib.sha256(vote_data.encode('utf-8')).hexdigest()

def create_genesis_block():
    return VoteBlock(0, date.datetime.now(), "0", 0, "0")

def add_vote(vote_chain, previous_block, student_id, candidate_id, db):
    index = previous_block.index + 1
    timestamp = date.datetime.now()
    previous_hash = previous_block.hash
    vote = VoteBlock(index, timestamp, student_id, candidate_id, previous_hash)
    vote_chain.append(vote)
    db.insert_vote(vote)
    return vote

def print_votes(vote_chain):
    for vote in vote_chain:
        print(f'Index: {vote.index}')
        print(f'Timestamp: {vote.timestamp}')
        print(f'Student ID: {vote.student_id}')
        print(f'Candidate ID: {vote.candidate_id}')
        print(f'Previous Hash: {vote.previous_hash}')
        print(f'Hash: {vote.hash}')
        print('-------------')

def load_vote_chain(db):
    vote_chain = []
    existing_votes = db.get_all_votes()
    for vote in existing_votes:
        vote_chain.append(VoteBlock(vote[0], vote[1], vote[2], vote[3], vote[4]))

    if not vote_chain:  # If no existing votes, create genesis block
        vote_chain.append(create_genesis_block())
    
    return vote_chain