# view_expense.py
from data_store import expenses


def view_expenses(username):
    user_expenses = expenses[username]

    if len(user_expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("No.  Date        Category      Amount   Note")
    for i in range(len(user_expenses)):
        exp = user_expenses[i]
        print(i + 1, exp["date"], exp["category"], exp["amount"], exp["note"])
