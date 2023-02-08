tple = (1, "apple","orange","banana",2,3,4,5,6,"jasi",1.3)
print(tple)
print(tuple(tple))
print(len(tple))
print(tple[0]) #indexing 1
print(tple[-1]) #negative indexing 1.3
print(tple[0:3]) #slicing
print(tple[::-1]) #reverse
print(tple[:-5]) # remove last five elements. result (1,2,3)
print(tple[-4:-1]) # (5,6,'jasi')

# to update a tuple
tple = (1, "apple","orange","banana",2,3,4,5,6,"jasi",1.3)
y = list(tple)  #mutable datatype
y[0] = "plum"
tple = tuple(y)
print(tple)

#append - add to end of the tuple
y.append("jjx")
tple = tuple(y)
print(tple)

#add a tuple
b = ("jas","jasim")
tple += b
print(tple)

#remove - (jasim will be removed)
x = list(tple)
x.remove("jasim")
tple = tuple(x)
print(tple)

# del (result: error tupp is not defined)
#tupp = (1,3,4,5,6,7)
#del tupp
#print(tupp)

tupp1 = (1,3,4,5,6,7)
print(all(tupp1))

tupp2 = (1,3,4,5,6,7,False)
print(all(tupp2))



