"""
define factorial of number using class with function argument and return
"""

# class Emp:
#     def fact(self,n):
#         f = 1
#         for i in range(1,n+1):
#             f = f*i
#         return f
#
# obj = Emp()
# n = int(input('Enter the number:'))
# f = obj.fact(n)
# print('factorial is:',f)

# Recursion method
class Emp:
    def fact(sl,x):

       if x == 1:
            return 1
       else:
            return x*sl.fact(x-1)

obj = Emp()
n = int(input('Enter the number:'))
f = obj.fact(n)
print('factorial is:',f)
