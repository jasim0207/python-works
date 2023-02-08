 #half pyramid pattern with number

row = int(input("enter rows: "))
for i in range(1,row+1):
    for j in range(i):
        print(j+1,end=" ")
    print()


#reverse pattern from 10 to 1

rows = int(input("enter the rows: "))
for a in range(0,rows):
    for b in range(rows-a,0,-1):
        print(b,end=" ")
    print()

#full pyramid with star

rw = int(input("enter the rows: "))
rws = rw -1
for c in range(1,rw+1):
    for d in range(rws):
        print(end=" ")
    rws = rws - 1
    for e in range(c):
        print("*",end=" ")
    print()


