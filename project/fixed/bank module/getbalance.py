# Get Balance Function
from data_store import users


def get_balance(account: int) -> str:
    curr_balance = users[account]['balance']
    return f"Current Balance is: {curr_balance}"
