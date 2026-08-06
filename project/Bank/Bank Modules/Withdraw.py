#Withdraw

def withdraw(account:int,withdraw_amount:int)->str:
    curr_balance=users[account]['balance']
    if curr_balance>=withdraw_amount:
        users[account]['balance'] -=withdraw_amount
        SingleEmailSend(to_email=users[amount['email']],
                                subject="withdraw Alert",
                                body=f"{withdraw_amount} withdraw successful and \
                                    current balance is:{users[account]['balance']}"
                                ) 
        return f"{withdraw_amount} withdraw successful and \ current balance is:{users[account]['balance']}"
    return "Insufficient Amount"