"""
what are the different types of data types?
sequence data saving - list,set,tuple,dictionary
dictionary - can save key value pair
list - can save data sequentially

what are the type casting method- use for convert data type
int(), float(),str()
list(),dict(),tuple(),set()
typeof used for the get the type of the datatype

features of the list:
sequential,indexed,allow duplication,ordered,mutable,represent []
features of the set:
immutable, not ordered,no indexing, doesn't allow duplicates
features of the tuple:
immutable,ordered,indexed,
features of the dictionary:
save data as key value pair,indexed,mutable, there is no duplication for the keys, but values allow the duplication
key cannot be edited. values can be edit.


"""
# wap to check whether given number is positive ,negative or zero
a = -1
if a>0:
    print("Number is positive")
elif a <0:
    print("Number is negative")
elif a ==0:
    print("Number is Zero")
else:
    print("Invalid")

# largest of the number used in nested if
a,b,c=int(input('Enter first number:')),int(input('enter second number:')),int(input('enter third number:'))
if a >b:
    if a >c:
        print(a," a is largest number")
    else:
        print(c," c is largest number")
elif  b>c:
    print(b," b is largest number")
else:
    print(c,' c is largest number')