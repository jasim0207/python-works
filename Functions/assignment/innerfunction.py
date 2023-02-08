"""create an inner function to calculate the addition in the following way

# create an outer function that will accept two parameters,a and b
# create an inner function inside an outer function that will calculate the addition of a and b
# at last, an outer function will add 5 into addition and return it
"""
def calculator(a,b):
    def addition():
        c = a+b
        return c
    return addition()+5
print(calculator(4,4))
