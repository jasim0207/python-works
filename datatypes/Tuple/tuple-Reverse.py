"""
1.Reverse  tuple

2. tple = (1,2,40,30,20)
   tple = (1,2,40,[10,2,39],(30,20,10))

   to remove repeated elements from this tuple

to access the value 20 from the tuple

3.  check if all items in the tuple are same

4.  copy specific elements from one tuple to a new tuple

5. swap two tuples in python
"""
# to remove duplicates froma tuple
#tpl1 = (1,2,40,[10,2,30],(30,20,10),40)
tpl1 = (1,2,40,40)
a = [] # list are mainly used for mutabe
b = []
for elem in tpl1:
    if elem not in a:
        a.append(elem)
        #print("a",a)

print(tuple(a))



#1
tpl = (5,6,7,8)
print(tpl[::-1]) #reverse

tple = (1,2,40,30,20)
list1 = list(tple)
print(tple[4])
