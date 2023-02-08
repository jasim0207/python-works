def smart_divide(func):
    def inner(a, b):
        print("iam going to divide", a, "and", b)
        if b == 0:
            print("whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(4,2)
divide(0,0)
