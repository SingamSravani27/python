# Withdraw Function
import data_store
from data_store import users


def withdraw(account: int, withdraw_amount: int) -> str:
    curr_balance = users[account]['balance']
    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        data_store.save_users()
        return f"{withdraw_amount} withdraw successful and current balance is: {users[account]['balance']}"
    return "Insufficient Balance"
