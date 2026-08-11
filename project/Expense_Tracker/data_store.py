# data_store.py
# central place to store users and expenses, shared by all modules
import json
import os

USERS_FILE = "users_data.json"
EXPENSES_FILE = "expenses_data.json"


def load_users():
    if os.path.exists(USERS_FILE):
        f = open(USERS_FILE, "r")
        data = json.load(f)
        f.close()
        return data
    return {}


def save_users():
    f = open(USERS_FILE, "w")
    json.dump(users, f, indent=4)
    f.close()


def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        f = open(EXPENSES_FILE, "r")
        data = json.load(f)
        f.close()
        return data
    return {}


def save_expenses():
    f = open(EXPENSES_FILE, "w")
    json.dump(expenses, f, indent=4)
    f.close()


users = load_users()
expenses = load_expenses()
