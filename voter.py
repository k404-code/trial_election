import qr_scanner
import csv
from tabulate import tabulate
from admin import print_candidates
import election_process as ep
import keyboard

def main():
    start_voting()
    

def start_voting():
    while True:
        voter_ID = get_voter_id()
        auth_to_vote()
        voted_candidate = cast_vote()
        ep.main([voter_ID, voted_candidate])

        print("Press 'q' to exit")
        if keyboard.read_key() == 'q':
            print("Exiting..")
            break
    
def cast_vote():
    candidates = print_candidates()

    # Rest of the code for casting vote
    # Example: Ask for user input to cast vote
    while True:
        try:
            candidate_number = int(
                input("Enter the Sl. No of the candidate you want to vote for: ")
            )
            if 1 <= candidate_number <= len(candidates):
                selected_candidate = candidates[candidate_number - 1]
                return selected_candidate
            else:
                print("Invalid candidate number")
        except ValueError:
            print("Please enter a valid number")


def get_voter_id():
    voter_id = qr_scanner.get_studentid()
    print(f"Voter ID: {voter_id}")
    return voter_id

def auth_to_vote():
    password = 'election2024'

    while True:
        if password == input("Polling Officer, please enter the password to proceed: "):
            return True
        else:
            print("Incorrect password. Please try again.")

if __name__ == "__main__":
    main()
