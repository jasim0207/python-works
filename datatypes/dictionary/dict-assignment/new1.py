#2
listofdict = [{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
#print("the given dictionary is: ",listofdict)
newdict = {}
list1 = []
for d in listofdict: # d gives each dictionary
    #print(d)
    p = list(d.values()) # create list of values
    list1.append(p[0])
    list1.append(p[1]) # list1 contains all individual values in a single list
#print(list1)

for i in range(0,len(list1),2): # taking each 2nd item in list
    if list1[i] in newdict:
        rep = list1[i]
        # print(rep) # result = item1
        index = list1.index(rep) # finding index of repeated variable
        list1[index+1] = list1[index+1]+list1[i+1] # adding corresponding value
        # print(list1[index+1]) # result = 1150
        # print(list1[i+1]) - result = 750
        newdict[list1[i]] = list1[index+1] # updating value of repeated element
        # print(newdict[list1[i]]) -
    else:
        newdict.setdefault(list1[i],list1[i+1]) # adding values to dictionary as key:value
print("the combined dictionary is : ",newdict)
