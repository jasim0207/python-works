def sum():
    a = 10
    b = 20
    c = a+b
    return c
# calling sum() function in print statement
print("The sum is:",sum())

# defining the function
def func(name): #name - parameter
    print("Hi",name)
# calling the function
func("jasim") #jasim - Arguments

# Arbitrary Arguments - single parameters and multiple arguments
def sample(*name1):
    print("Hi dears, My name is ",name1)

sample("jasim","jasi")
sample("CU")