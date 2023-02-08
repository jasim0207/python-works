"""
setdefault():
--------------
if key is in the dictionary, return its value.
if not, insert key with a value of default and return default.
default defaults to none.
"""
# 3. write a program to create a dictionary from a string. note: track the count of the letters from the string.
# sample string = 'luminar'
str1 = 'luminar'
print("the given string is :",str1)
dict1 = {}
for index in range(1,len(str1)+1): # 1, 7+1 = 1, 8
    dict1.setdefault(index,str1[index-1])
    # print(str1[index-1]) - result : l u m i n a r
    # print(index,str1[index-1]) result :
       # 1 l
       # 2 u
       # 3 m
       # 4 i
       # 5 n
       # 6 a
       # 7 r
print("the corresponding dictionary of the given string is :",dict1)
