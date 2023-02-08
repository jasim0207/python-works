"""
using for in the dictionary - print the keys
#using methods to access specific values from the dictionary
keys()
values()
copy()
"""

dict = {"name":"jasim","age":30,"address":"chuloor","course":"python"}
print(dict)
print(type(dict))
print(dict["name"])
print(dict.copy())

for i in dict:
    print(i)

# only print keys
dict1 = {"name":"jasim","age":30,"address":"chuloor","course":"python"}
print(dict1)
print(type(dict1))

for i in dict1.keys():
    print(i)
#only print values
dict2 = {"name":"jasim","age":30,"address":"chuloor","course":"python"}
print(dict2)
print(type(dict2))

for i in dict2.values():
    print(i)

