"""
1.WAP to get a string from a given string where all occurances of it's first char
have been changed to '$', except the first char itself.
sample o/p: 'restart'
o/p: 'restar&t'

2, WAP for python function that takes a list of words and returns the length of the
   longest one
"""
#1.
str1 = 'restart'
str2 = str1[0]
str1 = str1.lower()
for i in range(1,len(str1)):
    if str1[i] == str1[0]:
        str2 = str2 + "$"
    else:
        str2 = str2+str1[i]
print(str2)

#1. another method
str3 = 'restart'
char = str3[0]
length = len(str1)
str3 = str3.replace(char,'$')
str3 = char + str3[1:]
print(str3)

#2.

lst = list(input("enter space separated words").split())
m=max(lst)
print(f'length of the longest word {m} is {len(m)}')