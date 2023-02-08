x = ('python','java','express')
y = enumerate(x)
print(tuple(y))


#
letters = [('a','A'),('b','B')] #list of tuples
for i, letters in enumerate(letters):
    #print(i,letters)
    print("letter #%d is %s %s" % (i,letters[0],letters[1]))


names = ['mukesh','roni','bijo']
ages = [24, 50, 18]
for i, (name, age) in enumerate(zip(names,ages)): #zip
    print(i,name,age)

names1 = ('jasi','hasee','akhi')
ages1 = (24,50,18)
