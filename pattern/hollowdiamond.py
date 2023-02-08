num = int(input("enter the num: "))
for i in range(num):
    print("   "*(num-i)+"*",end=" ")
    if i != 0:
        print("   "*(2*i)+"*",end=" ")
    print()
for i in range(num,-1,-1):
    print("   " * (num - i) + "*", end=" ")
    if i != 0:
        print("   " * (2 * i) + "*", end=" ")
    print()
