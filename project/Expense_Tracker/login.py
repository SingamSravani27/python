# login.py
from data_store import users


def login(username, password):
    if username in users:
        if users[username]["password"] == password:
            return True
    return False
