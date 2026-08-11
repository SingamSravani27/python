# dashboard.py
from data_store import expenses
from datetime import date


def total_expense(username):
    total = 0
    for exp in expenses[username]:
        total = total + exp["amount"]
    return total


def monthly_expense(username):
    current_month = date.today().strftime("%Y-%m")
    total = 0
    for exp in expenses[username]:
        if exp["date"].startswith(current_month):
            total = total + exp["amount"]
    return total


def today_expense(username):
    today_str = str(date.today())
    total = 0
    for exp in expenses[username]:
        if exp["date"] == today_str:
            total = total + exp["amount"]
    return total


def show_dashboard(username):
    print("----- DASHBOARD -----")
    print("Today's Expense:", today_expense(username))
    print("This Month's Expense:", monthly_expense(username))
    print("Total Expense:", total_expense(username))
