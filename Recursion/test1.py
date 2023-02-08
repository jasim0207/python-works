#factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1) #5! = 5*(5-1)!
print(fact(5))


#2
def fact1(a):
    if a == 1:
        return a
    else:
        return a * fact1(a - 1)
              #5*4*3*2*1

num = int(input("Enter the number"))
if num < 0:
    print("Invalid")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    print(f'Factorial of {num} is {fact1(num)}')
