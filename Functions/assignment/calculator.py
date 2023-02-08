def sum(a,b):
    print("Result:",a+b)
def sub(a,b):
    print("Result:",a-b)
def mul(a,b):
    print("Result:",a*b)
def div(a,b):
    print("Result:",a/b)
print("""
1.Addition
2.Subtraction
3.Multiplication
4.division
""")
choice=int(input(("Enter the choice(1/2/3/4):")))
a = int(input("Enter the num1:"))
b = int(input("Enter the num2:"))
if(choice==1):
    sum(a,b)
elif(choice==2):
    sub(a,b)
elif(choice==3):
    mul(a,b)
elif(choice==4):
    div(a,b)
else:
    print("invalid")



