import mymodule
while True:
    op = int(input("1.Create\n2.Search\n3.Remove\n4.Replace\nEnter your choice:"))
    if op == 1:
        mymodule.create()
    elif op == 2:
        mymodule.search()
    elif op == 3:
        mymodule.remove()
    elif op == 4:
        mymodule.replace()
    else:
        break
