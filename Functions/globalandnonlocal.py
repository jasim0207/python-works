def programing():

    def python():
        nonlocal name
        name = "jasim"

    def mean_stack():
        global name
        name = "nikil"

    def flutter():
        nonlocal name
        name = "Haseem"

    name = "Bijoy"

    python()
    flutter()
    mean_stack()
    print("coder is :" + name)

programing()
print(name)