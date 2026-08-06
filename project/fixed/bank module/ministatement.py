# Mini Statement Function
from data_store import users


def mini_statement(account: int) -> str:
    user = users[account]
    return (f"Account Number: {account}\n"
            f"Name: {user['username']}\n"
            f"Email: {user['email']}\n"
            f"Balance: {user['balance']}")
