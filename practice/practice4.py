#identity operators

a = ['apple','orange']
c = a
print(c)

x = a is c
print(x)

b = ['car','bike']
d = b
y = b is not d
print(y)

#logical operators
#and
num = 5
print(num>3 and num<10) # both conditions are true.
#or
num = 6
print(num>4 or num<7) # one condition is true.
#nor
num = 5
print(not(num>3 and num<10))




