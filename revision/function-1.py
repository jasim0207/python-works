
#oops - programs are based on class and object
#class - class is the way to bind functions and its related datas.
#object - instance of class or runtime entity of a class

#function- Repeated group of statements/we can create a function for particular task.

#mainly --two parts-- function definition and function calling
#return value- we can pass only from function definition to function calling is called return value

# function definition - till return
# def sum():
#     a,b=10,20
#     s=a+b
#     return s

# function calling
# s = sum()
# print('sum is:',s)
# note - return s and s= sum() - the both 's' are not same, their memory location is different.

#1
# def sum():
#     a,b=10,20
#     s=a+b
#     return s
# s = sum()
# print('sum is:',s)
# print('sum is:',sum())

#2. passing parameters
def sum (x,y):
    s =x+y
    return s

s=sum(100,200)
print('sum is:',s)

print('sum is:',sum(20,40))

#3.WAP factorial of a number using function with return type and function parameter
def fact(n):
    f=1
    for i in range(1,n+1):
        f =f*i
    return f
f = fact(5)
print('factorial is:',f)

#function parameters
#simple,Arbitrary,keyword default,parameter value,list

# def colour(x,y,z): - simple argument ex
# def colour(*args): - arbitrary argument ex
#     print(args[0])
#
# colour('red','white','pink')

# ex -2
# def colour(*args):
#     print(args[0]) - running
#     for i in args: - running
#         print(i)
#
# colour('red','white','pink')

# def colour(x,*args):
#     print('Normal argument',x)
#     for i in args:
#         print(i)
#
# colour('red','white','pink')

def colour(x,*r):
    print('Normal argument',x)
    for i in r:
        print(i)

colour('red','white','pink')

#keyword argument

def stud(str1,str2,str3):
    print('first :',str1)
    print('second:',str2)
    print('third:',str3)
stud(str2='anu',str1='acu',str3='una')

# keyword argument
def student(**kwargs):
    for i,j in kwargs.items():
        print('%s=>%s'%(i,j))
student(str2='anu', str1='acu', str3='una')


#

def student1(x,*args,**kwargs):
    print('simple argument:',x)
    for j in args:
        print(j)
    for i,j in kwargs.items():
        print('%s=>%s'%(i,j))
student1('aachu','varun','jasi',str2='Anu',str1='kiran',str3='Arun')

# default parameter

def dispaly(country='india'):
    print('i am from',country)
dispaly()
dispaly('America')

def dis(ls):
    for i in ls:
        print(i)
dis([10,20,30])








