n = int(input('enter the number: '))
for i in range(n):
    for s in range(i):
        print(" ",end='')
    for j in range(n-i):
        print("* ",end='')
    print()
for i in range(n):
    for s in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
#pyramid - equation
num = int(input("enter the num: "))
for i in range(num):
    print(" "*(num-i)+"* "*(i+1))