"""generate a python list all the even numbers between 4 qnd 30 using function"""
def even():
    a =[]
    for i in range(start,stop):
        if i % 2 == 0:
            a.append(i)
    print(a)
start = int(input("enter the initial value: "))
stop = int(input("Enter the stop value: "))
even()

# even numbers 
start1 = int(input("Enter the start num: "))
end = int(input("enter the end position"))

def EvenNums(a,b):
    v = []
    for i in range(a,b,2):
        v.append(i)
    return v
print(EvenNums(start,end))