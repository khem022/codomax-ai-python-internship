import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses():
    """Load expenses from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved expenses. Starting with an empty list.")
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
    except OSError as error:
        print(f"Error saving expenses: {error}")


def get_amount():
    """Ask the user for a valid positive expense amount."""
    while True:
        try:
            amount = float(input("Enter amount (₹): "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")


def add_expense(expenses):
    """Add a new expense."""
    print("\n--- Add Expense ---")

    title = input("Enter expense name: ").strip()
    if not title:
        print("Expense name cannot be empty.")
        return

    category = input("Enter category (Food/Travel/Shopping/etc.): ").strip()
    if not category:
        category = "Other"

    amount = get_amount()

    expense = {
        "title": title,
        "category": category,
        "amount": round(amount, 2),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    """Display all recorded expenses."""
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['date']} | "
            f"{expense['title']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f}"
        )


def show_total(expenses):
    """Display the total amount spent."""
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expense: ₹{total:.2f}")


def category_summary(expenses):
    """Display spending grouped by category."""
    print("\n--- Category Summary ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    for category, amount in sorted(summary.items()):
        print(f"{category}: ₹{amount:.2f}")


def delete_expense(expenses):
    """Delete an expense selected by its number."""
    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    try:
        number = int(input("Enter expense number to delete: "))
        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        removed = expenses.pop(number - 1)
        save_expenses(expenses)
        print(f"Deleted: {removed['title']} - ₹{removed['amount']:.2f}")

    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 35)
    print("       EXPENSE TRACKER")
    print("=" * 35)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Category Summary")
    print("5. Delete Expense")
    print("6. Exit")
    print("=" * 35)


def main():
    """Run the Expense Tracker application."""
    expenses = load_expenses()

    print("Welcome to the Python Expense Tracker!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Thank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
