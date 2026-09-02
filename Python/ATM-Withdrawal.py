balance = 5000;
amount = float(input("Enter withdrawal amount: "));

if amount <= 0:
    print("Invalid Amount");
elif amount > balance:
    print("Insufficient balance")
else: 
    balance = balance - amount;
    print("Withdrawal successfull! ✅")