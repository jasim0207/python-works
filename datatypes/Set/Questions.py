"""
1. add a list of elements to a set

2. get only unique items from two sets

3. check if two sets have any elements in common.
  if yes, display the common elements

4. Remove items from set1 that are not common to both set1 and set2
"""
#convert the list to set
a = set()
b = [1,2,3,4,5,6,2,1]
a = set(b)
print(a)
print(type(a))

# 1.Add a list of elements to set?
set4 = {1,2,3,4,5}

# list of elements to add
list_add = [6,7,8]

# add all elements of list to set
set4.update(list_add)
print(set4)

# 2. get unique items from two sets
# uncommon elements
st1 = {1,2,3,4,5}
st2 = {4,5,6,7,8}

#print("unique items from 2 sets",A | B)
print("uncommon",st1.union(st2))

# 3. check if two sets have any elements in common.
  # if yes, display the common elements ?
set5 = {10,20,30,40,50}
set6 = {30,40,50,60,70}

if set5.isdisjoint(set6):
    print("Two sets have no items in common")
else:
    print("Two sets have items in common")
    print(set5.intersection(set6))

# 4. Remove items from set1 that are not common to both set1 and set2
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

#print('Difference = ', set1 & set2)
set1.intersection_update(set2)
print(set1)

# difference_update
set11 = {11,12,13,14,15}
set12 = {13,14,15,16,17}

set11.difference_update(set12)
print(set11)