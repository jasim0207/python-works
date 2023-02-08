#calculator
choice = input("enter a choice : +,-,*,/")
a = int(input("enter a first number: "))
b = int(input("enter a second number: "))

if choice=='+':
    print("sum is ", a+b)
elif choice=='-':
    print("difference is ", a-b)
elif choice=='*':
    print("multipy ", a*b)
elif choice=='/':
    print("div is ", a/b)

else:
    print("invalid")

