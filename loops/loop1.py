#loop - iterate
#for loop
name = 'jasim'
for i in name: #check every elements
 print(i)

for x in range(1,11): #output : print 1 to 10
 print(x)

list = [2,3,5,6]
n = 5
for y in list:
    c = n * y
    print(c)

list2 = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for a in range(0,len(list2)):
    sum = sum+list2[a]
    print("sum: " , sum)

#2
list3 = [1,2,3,4,5,6,7,8,9,10]
sum1 = 0
for b in list3:
    sum1 = sum1+b
    print("the sum is: ",sum1)

#1,2,3,4,5,6,,7,8,9,10
sum2 = 0
for c in range(1,11):
    sum2 = sum2+c
    print("the sum is: ",sum2)

# 3

n = int(input("enter the number: "))
for j in range(1,n):
    n = n+j
    print(n)
 # even number 1 to 10
for k in range(2,11,2): # odd number for k in range(1,11,3) or (1,11,2)
     print(k)

#multiplication
c = int(input("enter the number: "))
for l in range(1,11):
    d = c*l
    print(c,"*",l,"=",d)

#nested loop








