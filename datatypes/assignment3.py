#1. replace each special symbol with # in the following string
# str1 = '/*join is @developer % musician!!
# o/p - ##join is #developer # musician##

a = ('/*join is @developer % musician!!')
print(a.replace('/','#').replace('*','#').replace('@','#').replace('&','#').replace('%','#').replace('!','#'))

#another method



#2. append new string in the middle of a given string
# s1 = luminar
#s2 = python
# o/p = 'luminarpython'

s1 = 'luminar'
s2 = 'python'
a = s1[0:3]
b = s1[3:7]
print(a+s2+b)

#concantaneting a string to the middle of the another




