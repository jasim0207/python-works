# add items in the dictionary
d = {}
number = int(input('enter the number of elements in the dictionary:'))
for i in range(number):
    key=int(input('enter the key:'))
    value = input('enter the value:')
    d.update({key:value})
print(d)
