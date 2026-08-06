import register
import login
import getbalance
import withdraw
import deposit
import transfer
import ministatement
import logout
import emailsending
from data_store import users


# main
if __name__ == "__main__":
    print("Welcome to the Mini Bank")
    print("1. Login \n2. Register")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # call login function
        account = int(input("Enter your account number: "))
        password = input("Enter your password: ")
        login_val = login.login(account=account, password=password)

        if login_val:
            print("Login successful!")
            while True:
                print("\n1. Get Balance \n2. Withdraw \n3. Deposit \n4. Transfer \n5. Mini Statement \n6. Logout")
                menu_choice = int(input("Enter your choice: "))

                if menu_choice == 1:
                    print(getbalance.get_balance(account=account))

                elif menu_choice == 2:
                    amount = int(input("Enter withdraw amount: "))
                    result = withdraw.withdraw(account=account, withdraw_amount=amount)
                    print(result)
                    print(emailsending.singleEmailSend(
                        to_email=users[account]['email'],
                        subject="Withdrawal Alert - Mini Bank",
                        body=result
                    ))

                elif menu_choice == 3:
                    amount = int(input("Enter deposit amount: "))
                    result = deposit.deposit(account=account, deposit_amount=amount)
                    print(result)
                    print(emailsending.singleEmailSend(
                        to_email=users[account]['email'],
                        subject="Deposit Alert - Mini Bank",
                        body=result
                    ))

                elif menu_choice == 4:
                    receiver_account = int(input("Enter receiver account number: "))
                    amount = int(input("Enter transfer amount: "))
                    result = transfer.transfer(sender_account=account,
                                                receiver_account=receiver_account,
                                                transfer_amount=amount)
                    print(result)
                    print(emailsending.singleEmailSend(
                        to_email=users[account]['email'],
                        subject="Transfer Alert - Mini Bank",
                        body=result
                    ))

                elif menu_choice == 5:
                    print(ministatement.mini_statement(account=account))

                elif menu_choice == 6:
                    logout.logout()

                else:
                    print("Select your choice in between 1 to 6")
        else:
            print("Invalid login credentials")

    elif choice == 2:
        username = input("Enter user name: ")
        email = input("Enter user mail id: ")
        initial_deposit = int(input("Enter the initial deposit amount: "))
        password = input("Enter your new password: ")
        result = register.register(username=username,
                                     email=email,
                                     balance=initial_deposit,
                                     password=password)
        print(result)
        print(emailsending.singleEmailSend(
            to_email=email,
            subject="Welcome to Mini Bank!",
            body=f"Hi {username}, {result}. Thank you for registering with us!"
        ))

    else:
        print("Invalid choice, please select 1 or 2")
