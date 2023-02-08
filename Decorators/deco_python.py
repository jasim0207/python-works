"""
A python decorator is a function that takes in a function and returns by adding some functionality.

make_pretty() that takes a function as its argument and has a nested function named inner(), and returns the
inner function
"""
def make_pretty(func):
    def inner():
        print("i Got decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("iam ordinary")


ordinary()
