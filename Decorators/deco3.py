def upper_decor(fun):
    def wrapper():
        result = fun()
        return result.upper()
    return wrapper()

def hello_name():
    return "hello"
f = upper_decor(hello_name)
print(f)

