import json
import os
from datetime import datetime
from tabulate import tabulate

# File to store expenses
FILE_NAME = "expenses.json"

# Initialize data storage
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump([], file)


def load_expenses():
    """Load expenses from the file."""
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    """Save expenses to the file."""
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    """Add a new expense."""
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., Food, Transport): ")
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    date = date if date else datetime.now().strftime("%Y-%m-%d")

    expense = {"amount": amount, "category": category, "description": description, "date": date}
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses():
    """View all expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print("\nExpenses:")
    print(tabulate(expenses, headers="keys", tablefmt="grid"))


def delete_expense():
    """Delete an expense."""
    view_expenses()
    expenses = load_expenses()
    index = int(input("Enter the index of the expense to delete: ")) - 1

    if 0 <= index < len(expenses):
        deleted = expenses.pop(index)
        save_expenses(expenses)
        print(f"Deleted expense: {deleted}")
    else:
        print("Invalid index.")


def export_to_csv():
    """Export expenses to a CSV file."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses to export.")
        return

    file_name = "expenses.csv"
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["amount", "category", "description", "date"])
        writer.writeheader()
        writer.writerows(expenses)

    print(f"Expenses exported to {file_name}")


def main():
    """Main menu."""
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Export to CSV")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            export_to_csv()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

