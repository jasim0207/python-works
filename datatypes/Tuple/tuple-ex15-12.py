#3 check if  all items in the tuple are same
print('\n check if all items in the tuple are same')
#tup =(1,1,1,1,1,1)
tup = (1,2,10,15,16)
f = 1
for i in tup:
    for j in range(i,len(tup)-1):
        if tup[i] != tup[j+1]:
            f = 0
            break

if f == 1:
    print("same")
else:
    print("Not same")

#another method
tup1 =(1,2,5,6,7)
tup1 = set(tup1)
if len(tup) == 1:
    print("same")
else:
    print("not same")

#4 copy specific elements to one tuple to a new tuple



