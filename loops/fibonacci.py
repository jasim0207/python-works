#sum of n natural numbers
n = int(input("enter the number: "))
i = 1
sum = 0
while i <=n:
    sum = sum+i
    i = i+1
print(sum)

#fibanocci
#0,1,1,2,3,5,8

#fibanocci
n = int(input("enter the number: "))#input
n1 = 0
n2 = 1
sum = 0
while(n1<=n):
    sum = n1+n2
    n1 = n2
    n2 = sum
    print(n1)

#factorial of number
n = int(input("enter the number: "))
p = 1
i = 1
while i <= n:
    p = p*i
    i = i+1
print("Factorial of %d is %d"%(n,p))

