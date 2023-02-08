#for i in ls:
#  print(i)
#dis([10,20,30])

l = []
def create():
    number = int(input('enter the number of elements in the list:'))
    for i in range(number):
        item = int(input('enter the item:'))
        l.append(item)
    print(l)
def search():
    item = int(input('enter the item to be searched:'))
    if item in l:
        print('found')
    else:
        print('not found')

def remove():
    item = int(input('enter the item to be removed:'))
    if item in l:
        l.remove(item)
    else:
        print('item not fount in the list')
    print(l)
def replace():
    old = int(input('enter the item to be replaced:'))
    new = int(input('enter the item to be replaced:'))

    for i in range(len(l)):
        if l[i]==old:
            l[i]=new
    print(l)

while True:
    op = int(input("1.Create\n2.Search\n3.Remove\n4.Replace\nEnter your choice:"))
    if op == 1:
        create()
    elif op == 2:
        search()
    elif op == 3:
        remove()
    elif op == 4:
        replace()
    else:
        break
#create()
#search()
#remove()
#replace()

