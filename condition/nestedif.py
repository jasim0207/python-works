#nestedif
a = 35
if a > 10: # if a < 10: it is false, second condition is true so
    print("above Ten ")
    if a < 30:
        print("above thirty")
    else:
        print("not above 30")
else:
    print("invalid")

