# def factorial(no):
#     if no == 1:
#         return 1
#     else:
#         return no * factorial(no-1)
#
# print("factorial of a number is: ", factorial(5))

def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)

f=factorial(5)
print('factorial of 5 is',f)

#5*4!---5*24 = 120
#4*3!---4*6 = 24
#3*2!---3*2 = 6
#2*1!---2
