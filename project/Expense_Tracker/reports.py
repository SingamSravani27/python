# reports.py
from data_store import expenses


def generate_report(username):
    user_expenses = expenses[username]

    if len(user_expenses) == 0:
        print("No expenses to report yet.")
        return

    totals = {}
    for exp in user_expenses:
        cat = exp["category"]
        if cat in totals:
            totals[cat] = totals[cat] + exp["amount"]
        else:
            totals[cat] = exp["amount"]

    print("----- CATEGORY WISE REPORT -----")
    for cat in totals:
        print(cat, ":", totals[cat])
