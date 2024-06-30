import qr_scanner
import election_process as ep
import keyboard
from database import Database
from tabulate import tabulate

def main():
    start_voting()

def start_voting():
    db = Database(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    db.create_tables()  # Ensure the tables are created if they don't exist

    while True:
        voter_ID = get_voter_id()
        auth_to_vote()
        voted_candidate = cast_vote(db)
        ep.main([voter_ID, voted_candidate])

        print("Press 'q' to exit")
        if keyboard.read_key() == 'q':
            print("Exiting..")
            break

    db.close()  # Close the database connection

def cast_vote(db):
    candidates = print_candidates(db)
    # Rest of the code for casting vote
    # Example: Ask for user input to cast vote
    while True:
        try:
            candidate_number = int(
                input("Enter the ID of the candidate you want to vote for: ")
            )
            if any(candidate[0] == candidate_number for candidate in candidates):
                selected_candidate = next(candidate for candidate in candidates if candidate[0] == candidate_number)
                return selected_candidate
            else:
                print("Invalid candidate ID")
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

def print_candidates(db):
    candidates = db.get_all_candidates()
    # Prepare data for tabulate
    table = []
    for candidate in candidates:
        table.append([candidate[0], candidate[1], candidate[2]])
    # Print the candidates in tabular format
    headers = ["ID", "Candidate", "Forum"]
    print(tabulate(table, headers, tablefmt="grid"))
    return candidates

if __name__ == "__main__":
    main()
