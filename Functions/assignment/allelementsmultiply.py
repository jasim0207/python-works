"""write  a program to multiply all elements in  list using function"""

def multiply(a):
    mul = 1
    for i in a:
        mul = mul*i
    print("multiply is: ",mul)
a = [1,2,3,4,5]
multiply(a)
