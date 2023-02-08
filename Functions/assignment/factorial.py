"""write a python program to find the factorial of a number using function"""

def factorial(n):
    fact = 1
    i =1
    while(i<n):
        fact = fact*i
        i = i+1
    print("The factorial is: ",fact)
n = int(input("Enter num: "))
factorial(n)

#
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n = int(input("enter number: "))
print(fact(n))

