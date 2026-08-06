##Login Function
def login(account:int,password:str)->bool:
    if account in users:
        if users[account]['password'] == password:
            return True
        return False
    return False