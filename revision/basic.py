d = 'hhh'
g = '''hai
are 
you
'''
print(g)
"""
variable = it is a user defined token
variable or identifier
there is no particular meaning for the variable

keyword = pre defined token, it's already defined, it has particular meaning,
cannot be edit.
python has few keywords
keywords = int,str,dict,list

what are the operators?
arithmetic operators - +,-,*,/(normal division),%(reminder),**(exponent),//(floor division)-do not have decimal values
logical operators  - AND, OR, NOT
comparison operators - <,>,<=,>=,==,
x = 10 it is assignment operator
x+= 10 compound assignment
bitwise operators - change the input into bit and then compare.
logical AND - compare the input we give.


"""
a,b=10,20 # multiple values to multiple variables
x = y = 100 # single value to the multiple variables
"""
How to swap the variable?
"""
a = 10
b = 20

t = a
a = b
b = t

a = a+b # 30
b = a-b # 10
a = a-b # 20

# easy swapping method
# a,b=10,20
# a,b=b,a  #python allowing these method

#swapping values
a,b=int(input('enter first number:')),int(input('enter second number:'))
a,b=b,a
print('a=',a)
print('b=',b)


