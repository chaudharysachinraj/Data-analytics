balance = 5000

while True:
    print("\n===== ATM SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Amount deposited successfully!")
            print("Updated balance:", balance)
        else:
            print("Invalid amount!")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance = balance - amount
            print("Please collect your cash.")
            print("Updated balance:", balance)

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice! Please try again.")