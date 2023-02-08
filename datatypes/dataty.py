#data types in python
"""
#doc String
"""
"""
data types difference (explain)
1.mutable or immutable
2.ordered or unordered
3.allow duplicate or not
4.syntax
5.keywords
6.index check


"""



#Number-immutable
x = 5.1
print(x)

#String #immutable - we cannot change the value.-(string)set of charachters  indexed.
name = "jasi"
age = "20"
print(type(name))
print(type(age))
#list - mutable
list1 = [1,2,3,45,6,6]
print(type(list1))
#dictionary-mutable, maping , key value pairs element contains, key must be unique, do not allow the duplicates
dict = {"name": "jasi"}#{"age": 12}
print(type(dict))
#set-immutable datatype (unindexed), unordered,keyword set, duplicate elements not allowed
a = {1,2,3}
print(type(a))
#tuple-immutable
a = ("jasim","jasi","jas")#brakets is not mandatory
print(type(a))
# string indexing
str2 = "Hello world"
print(str2[-2])
#string slicing - (forwarding indexing)-positive slicing
print(str2[0:2])
print(str2[2:5])
print(str2[7:10])

#negative indexing
print(str2[:-1])
print(str2[::-1])
print(str2[::-2])
print(str2[::-3])
print(str2[-1:-6:-1]) #world - dlrow
print(str2[-2:-6:-1]) #world - worl
print(str2[-7:-12:-1]) #hello - olleh

print(str2.upper())
print(str2.lower())
print(str2.capitalize())
print(str2.isupper())
print(str2.islower())
print(str2.isalpha())
print(str2.swapcase())
print(str2.title())