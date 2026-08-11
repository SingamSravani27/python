# add_expense.py
import data_store
from datetime import date
from categories import is_valid_category
from notify import send_email


def add_expense(username, category, amount, note):
    if not is_valid_category(category):
        return "Invalid category! check the category list."

    if amount <= 0:
        return "Amount must be greater than 0."

    expense = {
        "date": str(date.today()),
        "category": category.title(),
        "amount": amount,
        "note": note
    }

    data_store.expenses[username].append(expense)
    data_store.save_expenses()

    user_email = data_store.users[username]["email"]
    body = "Category: " + category.title() + "\nAmount: " + str(amount) + "\nNote: " + note
    send_email(user_email, "New Expense Added", body)

    return "Expense added successfully!"
