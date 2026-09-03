userName = "Sachin";
password = 123;

userInput = (input("Enter your Password: "))

if userName == userInput:

    userPasword = int(input("Enter your Password: "))
    if password == userPasword:
        print("Login successful!")
    else:
        print("Invalid password.")
else:
    print("User is not found.")