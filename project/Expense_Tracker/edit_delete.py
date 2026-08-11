# edit_delete.py
import data_store


def edit_expense(username, index, category, amount, note):
    user_expenses = data_store.expenses[username]

    if index < 1 or index > len(user_expenses):
        return "Invalid expense number."

    user_expenses[index - 1]["category"] = category.title()
    user_expenses[index - 1]["amount"] = amount
    user_expenses[index - 1]["note"] = note
    data_store.save_expenses()
    return "Expense updated successfully!"


def delete_expense(username, index):
    user_expenses = data_store.expenses[username]

    if index < 1 or index > len(user_expenses):
        return "Invalid expense number."

    user_expenses.pop(index - 1)
    data_store.save_expenses()
    return "Expense deleted successfully!"
