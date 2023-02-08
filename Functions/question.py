"""
1. write a python function to find the max of three numbers?
2. write a python function to sum all the numbers in a list?
3. write a python function to multiply all numbers in a list?

"""

#1
def maxx():
    lst = [1,5,7]
    a = max(lst)
    return a
print(maxx())

#2
def sum(lst1):
    s = 0
    for i in lst1:
        s = s+i
        i+=1
    return s
#lst1 =[1,2,3,4,5]
print(sum([1,2,3,4,5]))

#3
def mul(lst2):
    r = 1
    for i in lst2:
        r = r*i
        i+=i
    return r
print(mul(lst2=[1,2,3,4]))
