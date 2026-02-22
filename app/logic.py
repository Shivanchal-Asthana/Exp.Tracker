import json
import csv
import os

DATA_FILE = "expenses.json"


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(amount, category):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    expenses = load_expenses()
    expense = {
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    save_expenses(expenses)


def calculate_total():
    expenses = load_expenses()
    return sum(exp["amount"] for exp in expenses)


def export_csv(filename="expenses.csv"):
    expenses = load_expenses()
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["amount", "category"])
        writer.writeheader()
        writer.writerows(expenses)
