# Register Function
import data_store


def register(username: str, email: str, balance: int, password: str) -> str:
    account = data_store.next_account_number
    data_store.users[account] = {
        'username': username,
        'email': email,
        'password': password,
        'balance': balance
    }
    data_store.next_account_number += 1
    data_store.save_users()
    return f"Registration successful! Your account number is {account}"
