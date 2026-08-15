# main.py
import register
import login
import add_expense
import view_expense
import edit_delete
import categories
import dashboard
import budget
import reports

current_user = None

print("Welcome to Expense Tracker")

while current_user is None:
    print("1. Login")
    print("2. Register")
    choice = input("Enter your choice: ")

    if choice == "1":
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        if login.login(uname, pwd):
            print("Login successful!")
            current_user = uname
        else:
            print("Invalid username or password.")

    elif choice == "2":
        uname = input("Choose a username: ")
        email = input("Enter your email: ")
        pwd = input("Choose a password: ")
        print(register.register(uname, email, pwd))

    else:
        print("Invalid choice")

while True:
    print("\n       EXPENSE TRACKER MENU      ")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. View Categories")
    print("6. Dashboard")
    print("7. Set Budget")
    print("8. Check Budget")
    print("9. Reports")
    print("10. Logout")

    choice = input("Enter your choice: ")

    if choice == "1":
        categories.show_categories()
        cat = input("Enter category: ")
        amt = float(input("Enter amount: "))
        note = input("Enter note: ")
        print(add_expense.add_expense(current_user, cat, amt, note))

    elif choice == "2":
        view_expense.view_expenses(current_user)

    elif choice == "3":
        view_expense.view_expenses(current_user)
        idx = int(input("Enter expense number to edit: "))
        cat = input("Enter new category: ")
        amt = float(input("Enter new amount: "))
        note = input("Enter new note: ")
        print(edit_delete.edit_expense(current_user, idx, cat, amt, note))

    elif choice == "4":
        view_expense.view_expenses(current_user)
        idx = int(input("Enter expense number to delete: "))
        print(edit_delete.delete_expense(current_user, idx))

    elif choice == "5":
        categories.show_categories()

    elif choice == "6":
        dashboard.show_dashboard(current_user)

    elif choice == "7":
        amt = float(input("Enter monthly budget: "))
        print(budget.set_budget(current_user, amt))

    elif choice == "8":
        print(budget.check_budget(current_user))

    elif choice == "9":
        reports.generate_report(current_user)

    elif choice == "10":
        print("Bye bye, see you later!")
        break

    else:
        print("Invalid choice")
