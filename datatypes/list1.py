my_list = [1,2,3,4,"welcome"]
my_list.insert(3,"jas")
print(my_list)

myis = [1,2,3,4]
myis.extend(my_list)
print(myis)
#append()
myis.append('hai')
print(myis)
#remove()
myis.remove('hai')
print(myis)
#insert()
myis.insert(3,'jasi')
print(myis)
#pop.() last number poped pop(0) first element poped
a = [1,2,3,4,5]
a.pop(0)
print(a) # 1 will be poped
#copy()
b = ['bird', 1,4,5]
nw_list = b.copy()
print(nw_list)
#clear
c = [5,6,7]
list1 = c.clear()
print(list1)
#index
d = [7,8,9]
list2 = d.index(9)
print(list2)
#sort
e = [3,2,1]
list3 = e.sort()
print(list3)
#reverse
f = ['jasim']
list4 = f.reverse()
print(list4)






