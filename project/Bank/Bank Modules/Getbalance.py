## Get Balance
def balance(account:int)->str:
    curr_balance = users[account]['balance']
    return f"Current Balance is:{curr_balance}"