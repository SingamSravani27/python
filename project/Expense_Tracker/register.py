# register.py
import data_store


def register(username, email, password):
    if username in data_store.users:
        return "Username already exists! Try a different one."

    data_store.users[username] = {
        "email": email,
        "password": password,
        "budget": 0
    }
    data_store.expenses[username] = []
    data_store.save_users()
    data_store.save_expenses()
    return "Registration successful! Welcome, " + username
