# Deposit Function
import data_store
from data_store import users


def deposit(account: int, deposit_amount: int) -> str:
    users[account]['balance'] += deposit_amount
    data_store.save_users()
    return f"{deposit_amount} deposit successful and current balance is: {users[account]['balance']}"
