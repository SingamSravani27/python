# DATA BASE
# import requirements
from emailsend import SingleEmailSend
"""
users={
        Account:{
                'name':"Username,
                'email':User email,
                'balance':5000,
                'password':password
                }
        }
        
"""


'''users = {
    1001: {
        'name': "Sravani",
        'email': "singamsravani410@gmail.com",
        'balance': 5000,
        'password': '1001'
    },
    1002: {
        'name': "Akhila",
        'email': "Akhilashetty@gmail.com",
        'balance': 4000,
        'password': '1002'
    }
}


##Register function
def register(username:str, email:str, balance:int, password:str)->str:
    return "Register page under development process"

##Login Function
def login(account:int,password:str)->bool:
    if account in users:
        if users[account]['password'] == password:
            return True
        return False
    return False
    

## Get Balance
def balance(account:int)->str:
    curr_balance = users[account]['balance']
    return f"Current Balance is:{curr_balance}"
    

#Withdraw
def withdraw(account:int,withdraw_amount:int)->str:
    curr_balance=users[account]['balance']
    if curr_balance>=withdraw_amount:
        users[account]['balance'] -=withdraw_amount
        ## send email
        SingleEmailSend(to_email=users[amount['email']],
                        subject="withdraw Alert",
                        body=f"{withdraw_amount} withdraw successful and \
                            current balance is:{users[account]['balance']}"
                        ) 


        return f"{withdraw_amount} withdraw successful and \ current balance is:{users[account]['balance']}"
    return "Insufficient Amount"

    

#Deposite Function
def Deposite(account:int,Deposite_amount:int)->str:
      

      users[account]['balance'] +=Deposite_amount
      return f"{Deposite_amount} deposite successful and \ current balance is:{users[account]['balance']}"
         
    

##Transfer Function
def transfer(from_acc:int, to_acc:int, transfer_amount:int):
     print("user in transfer page")
    

# Ministatement Function
def Ministatement(account:int):
     return "Ministatement page under development process"
    

#logout Function
def logout():
     print("Bye Bye Buddy, see you later")'''


from Login import login
from Deposit import Deposite
from Getbalance import balance
from Logout import logout
from Ministatement import Ministatement
from Register import register
from Transfer import transfer
from Withdraw import withdraw
#main
if __name__ == "__main__":
    print("Welcome to the mini bank")
    print("1.Login \n 2.Register")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        #call login function
        account= int(input("Enter Your Account Number:"))
        password = input("Enter Your Password:")
        login_val = login(account=account, password=password)
        while login_val:
            print("1.Get Balance \n 2.withdraw \n 3. Deposit \n 4. Transfer \n 5.Mini statement \n 6. logout ")
            choice = int(input("Enter your choice:"))
            if choice == 1:
            #call balance functions

                print(balance(account=account))

            elif choice == 2:
             #call withdraw function
                amount = int(input("Enter withdraw amount:"))
                print(withdraw(account=account, withdraw_amount=amount))

            elif choice == 3:
                 #call deposit function
                amount =int(input("Enter Deposite amount:"))
                print(Deposite(account=account, Deposite_amount=amount))

            elif choice == 4:
                reciever = int(input("Enter recieve amount:"))
                amount = input("Enter Transfer amount:")
                print(transfer(from_acc=account, to_acc=reciever, transfer_amount=amount))

            elif choice == 5:
                print(Ministatement(account=account))

            elif choice == 6:
                print(logout())

            else:
                print("Select your choice in between 1-6")
        else :
            print("Invalid Login credentials")   
    elif choice == 2:
        username = input("Enter user name:")
        email = input("Enter user email id:")
        initial_deposit = int(input("Enter the initial Deposit amount:"))
        password = input("Enter your new password:")
        print(register(username=username,
                       email=email,
                       blance=initial_deposite,
                       password=password))
    else:
        print("Invalid choice, please select 1 or 2")



        

            





