#sum of natural numbers
n = int(input("enter the number: "))
i = 1
sum = 0
while i<=n:
    sum = sum+i
    i = i+1
print(sum)

a = int(input("enter the num: "))
b = 1
sum1 = 0
while b<=a:
    sum1 = sum1+b
    b = b+1
print(sum1)



#fibanocci
n = int(input("enter the number: "))
n1 = 0
n2 = 1
sum = 0
while(n1<=n):
    sum = n1+n2
    n1 = n2
    n2 = sum
    print(n1)
#2
a = int(input("enter num: "))
a1 = 0
b1 = 1
sum = 0
while(a1<=a):
    sum = a1+b1
    a1 = b1
    b1 = sum
    print(a1)
#factorial of a number
n = int(input("enter the number: "))
a = 1
b = 1
while(b<=n):
    a = a*b
    b = b+1
print("factorial of %d is %d"%(n,a))



