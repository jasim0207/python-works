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
