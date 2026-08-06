# Central data store - shared by all modules
# key = account number, value = dict with username, email, password, balance
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "users_data.json")


def load_users():
    """Load saved users from the json file (if it exists) so data is not lost between runs"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            # JSON always saves keys as strings, so convert account numbers back to int
            return {int(acc): details for acc, details in data.items()}
    return {}


def save_users():
    """Save the current users dictionary to the json file - call this after any change"""
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)


users = load_users()
next_account_number = max(users.keys()) + 1 if users else 1001
