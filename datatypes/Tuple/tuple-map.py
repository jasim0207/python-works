#list of string

#l = ['sat','bat','cat','mat']
l = ('sat','bat','cat','mat')
# map() can listify the list of strings individually
#test = list(map(list,l))
#test = list(map(set,l))
#test = list(map(tuple,l))
test = tuple(map(tuple,l))
print(test)
