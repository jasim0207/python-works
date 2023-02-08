#break
for x in range(6):
    #print(x)
    if x == 3:
        break
    print(x)


#continue - (skip the 3 in the program-(if y == 3:)
for y in range(9):
    if y == 3:
        continue
    print(y)
else:
    print("finally finished")

#if the loop breaks, the else block is not executed.

#pass (empty statement)
for z in range(9):
    pass
