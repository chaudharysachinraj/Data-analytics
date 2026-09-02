# marks = 65 
# if marks >= 40 :
#     print("pass")
# else:
#     print("Fail")

# marks = 30 
# if marks >= 40 :
#     print("Pass")
# else:
#     print("Fail")



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
