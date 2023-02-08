"""
pop()
popitem()
del keyword
clear()
"""
# pop() is used for to remove items with the specified key name.
car1 = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1964
}
car1.pop("model")
print(car1)

# popitem() method removes the last inserted item.
car2 = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1964
}
car2.popitem()
print("popitem: ",car2)

# del keyword
car3 = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1964
}
del car3["model"]

print(car3)

#delete dictionary
car4 = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1964
}
del car4
print(car4) # this will cause an error because "car4" no longer exists.




