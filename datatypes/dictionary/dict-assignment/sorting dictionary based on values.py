dict1 = {1:2,3:4,4:3,2:1,0:0}
print("The given dictionary is : ",dict1,"\n")
val = list(dict1.items()) #creates a list of tuples of key: value pairs
#print(val)
newval = []
newvalf = []

for i in val:
    #print(i)#key:value pair
    irev = i[::-1]
    #print("rev:",irev)#ordering value: key format
    newval.append(irev)                 #appending value:
#print(newval)
val.clear()                              #clearing key:value:
newval.sort()
print(newval)#sorting based on values value:key

for i in newval:
    irevf = i[::-1]
    val.append(irevf)
  # print(val,"/n")

for i in (newval[::-1]):         #taking reverse
    i = i[::-1]               #reversing back to
    newvalf.append(i)        #appending descends
#print(newvalf,"/n")

print("the dictionary in ascending order of value is : ",dict(val),"\n")
print("the dictionary in ascending order of value is : ",dict(newvalf))