#convert string to tuple
a = "jasim"
print(type(a))
tpl = tuple(a)
print(tpl)

#convert list to tuple
lst = ["car","bike","bus"]
print(type(lst))
tpl1=tuple(lst)
print(tpl1)

#find repeated items from the tuple
tpl2 = ("hi","hi",1,2,4,5,6)
print(tpl2.count("hi"))