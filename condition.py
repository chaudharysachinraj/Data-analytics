a=int(input())
b=int(input())
choice=input("enter your choice +, -, *, /: ")
if choice == '+':
    print(a+b)
elif choice == '-':
    print (a-b)
elif choice == '*':
    print(a*b)
elif choice == '/':
    print (a/b)
else :
    print ("Wrong choice! Please chose =, -, *, /")
