# Transfer Function
import data_store
from data_store import users


def transfer(sender_account: int, receiver_account: int, transfer_amount: int) -> str:
    if receiver_account not in users:
        return "Receiver account does not exist"
    if users[sender_account]['balance'] < transfer_amount:
        return "Insufficient Balance"
    users[sender_account]['balance'] -= transfer_amount
    users[receiver_account]['balance'] += transfer_amount
    data_store.save_users()
    return f"{transfer_amount} transferred successfully to account {receiver_account}. Current balance: {users[sender_account]['balance']}"
