#Square
def square(num):
    return num**2
obj = square(9)
#print("The square of the number is: ",square(9))
print("The square of the number is: ",obj)

# string
def a_function(string):
    return len(string)
print("length of the string: ",a_function("Luminar"))
print("length of the string: ",a_function("python"))

def sum(*n):
    s = 0
    for i in n:
        n = n*((n+1)/2)

    print("the sum = : ",s)
sum(10,60)
