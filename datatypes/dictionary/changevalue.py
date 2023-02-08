car = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1964
}
car["year"] = 2018
print(car)

# update dictionary (another change method)

car1 = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1964
}
car1.update({"year":2020})
car1.update({"brand":"volksvagan","model":"polo"}) # change multiple items
print("update method: ",car1)


