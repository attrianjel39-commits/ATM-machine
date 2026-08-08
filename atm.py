balance = 10000
while True:
    print("press one Depositing money")
    print("press two for checking money")
    print("press three for cash widrawl")
    print("exit")
    
    choice = int(input("enter your choice: "))

    if choice == 2:
        print("Total balance in your account is: ", balance)
    elif choice == 1:
        Amount = float(input("Enter the Amount you want to Deposit. "))
        balance = balance+ Amount
        print("Amount Deposited Successfully.")
    
    elif choice == 3:
        Amount = float(input("Enter the Amount you want to widraw."))
        if Amount <= balance:
            balance = balance - Amount
            print("Money left: ", balance)
        else:
            print("Money can not be widrawn")
    elif choice == 4:
        print("exiting the ATM mode")
        break               
    
    