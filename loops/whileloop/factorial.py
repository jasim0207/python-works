#factorial of number
n = int(input("enter the number: "))
nm = 1
i = 1
while i <= n:
    nm = nm*i
    i = i+1
print("Factorial of %d is %d"%(n,nm))

