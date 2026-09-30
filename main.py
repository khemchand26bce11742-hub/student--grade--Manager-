import csv
import os
from datetime import datetime

FILE = "expenses.csv"


def load_data():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", newline="") as file:
        return list(csv.DictReader(file))


def save_data(data):
    with open(FILE, "w", newline="") as file:
        fields = ["date", "type", "category", "amount", "description"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


def add_transaction(data):
    print("\n1. Income")
    print("2. Expense")

    choice = input("Choose type: ")

    if choice == "1":
        transaction_type = "Income"
    elif choice == "2":
        transaction_type = "Expense"
    else:
        print("Invalid choice.")
        return

    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "type": transaction_type,
        "category": category,
        "amount": amount,
        "description": description
    }

    data.append(transaction)
    save_data(data)

    print("Transaction added successfully!")


def show_transactions(data):
    if not data:
        print("\nNo transactions found.")
        return

    print("\n========== TRANSACTION HISTORY ==========")

    for item in data:
        print(
            item["date"], "|",
            item["type"], "|",
            item["category"], "| ₹",
            item["amount"], "|",
            item["description"]
        )


def show_summary(data):
    income = 0
    expense = 0

    for item in data:
        amount = float(item["amount"])

        if item["type"] == "Income":
            income += amount
        else:
            expense += amount

    balance = income - expense

    print("\n========== FINANCIAL SUMMARY ==========")
    print("Total Income : ₹", round(income, 2))
    print("Total Expense: ₹", round(expense, 2))
    print("Current Balance: ₹", round(balance, 2))


def search_category(data):
    category = input("Enter category to search: ").lower()
    found = False

    print("\n========== SEARCH RESULTS ==========")

    for item in data:
        if item["category"].lower() == category:
            print(
                item["date"], "|",
                item["type"], "| ₹",
                item["amount"], "|",
                item["description"]
            )
            found = True

    if not found:
        print("No transactions found for this category.")


def main():
    data = load_data()

    while True:
        print("\n================================")
        print("       SMART EXPENSE TRACKER")
        print("================================")
        print("1. Add Income/Expense")
        print("2. View Transactions")
        print("3. Financial Summary")
        print("4. Search by Category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction(data)

        elif choice == "2":
            show_transactions(data)

        elif choice == "3":
            show_summary(data)

        elif choice == "4":
            search_category(data)

        elif choice == "5":
            print("Thank you for using Smart Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
