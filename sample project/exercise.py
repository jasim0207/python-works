#comparison
a = 5
b = 5
print(a==b)

a = 5
b = 5
print(a!=b)

a = 5
b = 5
print(a<=b)

a = 5
b = 5
print(a>=b)

a = 5
k = 5
print(a>b)

a = 5
b = 5
print(a<b)

#calculator  1
#num1 = input("Enter a number: ")
#num2 = input("Enter a another number: ")
#result = int(num1) + int(num2)
#result = float(num1) + float(num2)
#print(result)

#calculator in single line

#print(eval(input("enter an expression")))

#calculator 2

def add(P,Q):
  return P + Q
def subtract(P,Q):
    return P - Q
def multiply(P,Q):
    return P * Q
def divide(P,Q):
    return P / Q


print("please select the operation.")
print("a. Add")
print("b. subtract")
print("a. multiply")
print("a. divide")

choice = input("please enter the choice (a/b/c/d): ")

num1 = int(input("please enter the first number: "))
num2 = int(input("please enter the second number: "))

if choice == 'a':
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == 'b':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == 'c':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == 'd':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("invalid input")
#if
a = 33
b = 200
if b > a:
    print("b is greater than a")

#Elif
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
#while
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 1 ")

#Exercise






