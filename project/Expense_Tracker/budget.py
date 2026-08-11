# budget.py
import data_store
from dashboard import monthly_expense


def set_budget(username, amount):
    data_store.users[username]["budget"] = amount
    data_store.save_users()
    return "Monthly budget set to " + str(amount)


def check_budget(username):
    budget = data_store.users[username]["budget"]

    if budget == 0:
        return "No budget set yet. please set a budget first."

    spent = monthly_expense(username)
    remaining = budget - spent

    if remaining < 0:
        return "Warning! you have exceeded your budget by " + str(abs(remaining))
    return "You have " + str(remaining) + " remaining out of " + str(budget) + " this month."
