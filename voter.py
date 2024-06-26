import qr_scanner
import csv
from tabulate import tabulate


def main():
    get_voter_id()


def cast_vote():
    # Read candidates from candidates.csv
    with open("candidates.csv", "r") as file:
        reader = csv.DictReader(file)
        candidates = list(reader)

    # Prepare data for tabulate
    table = []
    for slno, candidate in enumerate(candidates, start=1):
        table.append([slno, candidate["name"], candidate["forum"]])

    # Print the candidates in tabular format
    headers = ["Sl. No", "Candidate", "Forum"]
    print(tabulate(table, headers, tablefmt="grid"))

    # Rest of the code for casting vote
    # Example: Ask for user input to cast vote
    try:
        candidate_number = int(
            input("Enter the Sl. No of the candidate you want to vote for: ")
        )
        if 1 <= candidate_number <= len(candidates):
            selected_candidate = candidates[candidate_number - 1]
            break
        else:
            print("Invalid candidate number")
    except ValueError:
        print("Please enter a valid number")


def get_voter_id():
    voter_id = qr_scanner.get_studentid()
    print(f"Voter ID: {voter_id}")
    cast_vote()


if __name__ == "__main__":
    main()
