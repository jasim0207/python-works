#Arguments (args)/positional args
def my_function(msg1,msg2):
    print(msg1 +  " " + msg2)
my_function("How are you","Hi")

#Arbitrary Arguments
def my_func(*names):
    print("Hi",names,"How r u")
my_func('jas','jasim','cu')
my_func('jazz')
my_func('jinn')

# keyword Arguments
def my_function(Name1, Name2, Name3):
    print("last name is " + Name2)

my_function("jin", Name3= "jack",Name2="Jerrin")

# Arbitrary keyword arguments(**kwargs)
def my_function(**name):
    print("The last name is "+ name["lname"])
my_function(fname = "jasii",lname="cu")


# default value
def my_function(country = "Norway"):
    print("Im from "+ country)

my_function("sweden")
my_function("India")
my_function()

def sum(a,b):
    print("sum is :",a+b)
sum(5,6)




