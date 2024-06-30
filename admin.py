from tabulate import tabulate
from database import Database

# Set the demo password
demo_password = "password123"

# Function to authenticate the user
def authenticate():
    password = input("Enter the password: ")
    if password == demo_password:
        return True
    else:
        return False

# Function to add a candidate
def add_candidate(db):
    name = input("Enter the candidate's name: ")
    forum = input("Enter the candidate's forum: ")
    candidate_id = db.insert_candidate(name, forum)
    print(f"Candidate added successfully with ID {candidate_id}!")

# Function to remove a candidate
def remove_candidate(db):
    name = input("Enter the candidate's name: ")
    db.remove_candidate(name)
    print("Candidate removed successfully!")

# Function to view all candidates
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

# Main function
def main():
    db = Database(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    db.create_tables()  # Ensure the tables are created if they don't exist

    if authenticate():
        while True:
            print("Menu:")
            print("1. Add Candidate")
            print("2. Remove Candidate")
            print("3. View Candidates")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                add_candidate(db)
            elif choice == "2":
                remove_candidate(db)
            elif choice == "3":
                print_candidates(db)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Authentication failed.")
    print()

    db.close()  # Close the database connection

if __name__ == "__main__":
    main()
