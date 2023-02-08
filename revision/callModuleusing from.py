# from mymodule import create
# create() - we can call one by one using function (create(),search()). by using * we can call every function
# in the program.

from mymodule import *
while True:
    op = int(input("1.Create\n2.Search\n3.Remove\n4.Replace\nEnter your choice:"))
    if op == 1:
        create()
    elif op == 2:
        search()
    elif op == 3:
        remove()
    elif op == 4:
        replace()
    else:
        break