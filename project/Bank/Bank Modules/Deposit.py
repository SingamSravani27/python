#Deposite Function
def Deposite(account:int,Deposite_amount:int)->str:
    users[account]['balance'] +=Deposite_amount
    return f"{Deposite_amount} deposite successful and \ current balance is:{users[account]['balance']}"