import csv
from tabulate import tabulate

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
def add_candidate():
    name = input("Enter the candidate's name: ")
    forum = input("Enter the candidate's forum: ")
    with open("candidates.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, forum])
    print("Candidate added successfully!")

# Function to remove a candidate
def remove_candidate():
    name = input("Enter the candidate's name: ")
    candidates = []
    with open("candidates.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["name"] != name:
                candidates.append(row)
    with open("candidates.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Forum"])
        writer.writeheader()
        writer.writerows(candidates)
    print("Candidate removed successfully!")

# Function to view all candidates
def print_candidates():
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
    return candidates

# Main function
def main():
    if authenticate():
        while True:
            print("Menu:")
            print("1. Add Candidate")
            print("2. Remove Candidate")
            print("3. View Candidates")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                add_candidate()
            elif choice == "2":
                remove_candidate()
            elif choice == "3":
                print_candidates()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
                
    else:
        print("Authentication failed.")
    print()
    
# Run the main function
if __name__ == "__main__":
    main()
