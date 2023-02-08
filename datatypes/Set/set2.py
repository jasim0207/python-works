set_sap = {1,2,3,4,6}
print(set_sap)

set_sam = {1.0,2,4,"Hi",(1,2,3),(1,2,3,4)}
print(set_sam)
a = set([1,2,3,4])
print(type(a))

# mathematics operations
A = {1,2,3,4,5}
B = {4,5,6,7,8}

print('Unoin    =', A|B)
print('Intersection = ', A&B)
print('Difference = ', A - B)
print('Symmetric Diff =', A^B)
