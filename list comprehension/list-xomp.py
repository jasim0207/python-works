# list comprehension
# syntax:list=[expression for item in list if condition]
l = [x+3 for x in [1,2,3]]
print(l)

#print even number less than 25
l1 = [i for i in range(25) if i%2==0]

print(l1)

# find vowels from the string

v = [i for i in 'hai how are you?' if i in ['a','e','i','o','u']]
print(v)

# split the first letter from the word
str = 'hai how are you'
words= str.split()
# print(words) - return result as list
firstletter=[i[0] for i in words]
print(firstletter)

#return the item(word) contain 'e'?

colors = ['red','white','green','pink']
nwlst = [i for i in colors if 'e' in i]
print(nwlst)

# return all the items in the list except green.
colors = ['red','white','green','pink']
nwlst = [i for i in colors if i!='green']
print(nwlst)

# given built-in method use in list-comprehension
colors = ['red','white','green','pink']
nwlst = [i.upper() for i in colors ]
print(nwlst)

# working of the i expression - ex
colors = ['red','white','green','pink']
nwlst = ['hello' for i in colors ]
print(nwlst)

colors = ['red','white','green','pink']
nwlst = [i if i!='pink' else 'Blue' for i in colors]
print(nwlst)

words = 'haihowareyou'
ans = {i:len(i) for i in words}
print(ans)




