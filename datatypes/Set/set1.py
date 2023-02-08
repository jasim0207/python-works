"""
1. immutable
2. unordered
3. unindexed
4. duplicates not allowed

Set items are unchangable , but you can remove and items
"""
# creating set
numberSet = {1,2,3,4,3,2}
print(numberSet)

# creating empty set
emptySet = { }   # this creates empty dictionary
print(type(emptySet))

emptySet = set()  # this creates empty set
print(type(emptySet))


# set of mixed datatypes
my_set = {1.0, "Hello", (1,2,3)}
print(my_set)

# we can convert list to set using set function
set_with_list = set([1,2,3])
print(type(set_with_list))
print(set_with_list)