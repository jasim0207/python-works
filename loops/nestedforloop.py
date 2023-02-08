rows = int(input("enter the rows: ")) # user input
for i in range(1,rows+1): #rows
    #print(i)
    for j in range(i): #column
        #print(j)

        print("*",end=" ")
    print()
# inverted
row = int(input("enter the row: "))
for k in range(row+1,0,-1):
    for l in range(k-1):
        print("*",end=" ")
    print()


