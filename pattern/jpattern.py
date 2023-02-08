a ="*"

for i in range(1,6):
    for j in range(1,6):
        if (i==1) or (i>1 and j==3) or (i==5 and j<3):
            print(a, end='   ')
        else:
            print(" ",end ='  ')
    print("\n")



