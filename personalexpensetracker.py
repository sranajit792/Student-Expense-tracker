import json
from datetime import datetime

FILE_NAME = "expenses.json"


# ---------- File Handling ----------
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# ---------- Add Expense ----------
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food, Transport, etc.): ")
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

        if date == "":
            date = datetime.today().strftime("%Y-%m-%d")

        expense = {
            "amount": amount,
            "category": category,
            "date": date
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully.")

    except ValueError:
        print("Invalid amount. Please enter a number.")


# ---------- View Summary ----------
def view_summary(expenses):
    if not expenses:
        print("No expenses found.")
        return

    total = 0
    category_summary = {}

    for exp in expenses:
        total += exp["amount"]
        category = exp["category"]
        category_summary[category] = category_summary.get(category, 0) + exp["amount"]

    print("\n----- Expense Summary -----")
    print("Category-wise spending:")
    for cat, amt in category_summary.items():
        print(f"{cat}: ₹{amt}")

    print(f"\nTotal Spending: ₹{total}")


# ---------- Menu ----------
def menu():
    expenses = load_expenses()

    while True:
        print("\n----- Personal Expense Tracker -----")
        print("1. Add an Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_summary(expenses)

        elif choice == "3":
            print("Thank you for using Personal Expense Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")


# ---------- Program Start ----------
menu()
