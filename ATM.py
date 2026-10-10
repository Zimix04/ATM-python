import random

#constant - 1
LOAN_LIMIT = 1000

#variables - 2
securitycode = 0
name = ""
loan = 0.0
balance = 0.0
usage = True
loggedin = False
registered = False

#start menu - 3
while usage:
    print("\n==============================")
    print("\n  Welcome to the ATM System")
    print("\n==============================")
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Choose (1-3): "))

#register - 4
    if choice == 1:
        validity = False
        while not validity:
            name = input("\nAccount Name: ").strip().title()
            validity = not (name == "" or name.lower() == name.upper())
            if not validity:
                print("Error: Account name cannot be empty or be numbers")
            
        securitycode = random.randint(1000,9999)
        registered = True
        print("\n==============================")
        print("\nAccount created! Welcome,", name + "!")
        print("\nYour security code is,", securitycode)
        print("\n==============================")

#login - 5
    elif choice == 2:
        if not registered:
            print("\nNo account found. Please register first.")
        else:
            entercode = int(input("\nEnter your Security Code: "))
            while entercode != securitycode:
                print("Incorrect Code, Please try again.")
                entercode = int(input("\nEnter your Security Code: "))
            loggedin = True
            print("\n------------------------------")
            print("Login successful. Welcome,", name + "!")
            print("------------------------------")
#atm menu - 6              
            while loggedin:
                print("\n==============================")
                print("           ATM MENU")
                print("==============================")
                print("  Account:", name)
                print("  Balance:", balance)
                print("------------------------------")
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Loan")
                print("4. Logout")
                option = int(input("Choose (1-4): "))
#deposit - 7              
                if option == 1:
                    amount = float(input("\nEnter the amount of deposit: "))
                    if amount <= 0:
                        print("Invalid Amount...")
                    else:
                        if loan > 0:
                            payment = amount if amount <= loan else loan
                            loan -= payment
                            amount -= payment
                            print("Loan payment deducted:", payment)
                            print("Remaining loan:", round(loan, 2))

                        balance += amount
                        print("Added to balance:", amount)
                        print("New balance:", round(balance, 2))
#withdraw  - 8                      
                elif option == 2:
                    amount = float(input("\nEnter the amount to withdraw: "))
                    if amount <= 0:
                        print("Invalid Amount...")
                    elif amount > balance:
                        print("Insufficient balance.")
                    else:
                        balance -= amount
                        print("Withdrawn:", amount)
                        print("New balance:", round(balance, 2))
#loan  - 9       
                elif option == 3:
                    print("\nLoan limit:", LOAN_LIMIT)
                    print("Available to borrow:", LOAN_LIMIT - loan)
                    amount = float(input("Enter the loan amount: "))
                    if amount <= 0:
                        print("Invalid Amount...")
                    elif loan + amount > LOAN_LIMIT:
                        print("Loan exceeds the limit.")
                    else:
                        loan += amount
                        balance += amount
                        print("Loan approved:", amount)
                        print("New balance:", round(balance, 2))
#logout back to menu  - 10               
                elif option == 4:
                    loggedin = False
                    usage = True
                    print("\nYou have been logged out.")
                    print("Returning to the main menu...")

                else:
                    print("\nInvalid choice. Please select 1 or 4")

#exit fully - 11
    elif choice == 3:
        usage = False
        print("\nThank you for using our ATM, Goodbye!")
        
    else:
        print("\nInvalid choice. Please select 1 or 3")


