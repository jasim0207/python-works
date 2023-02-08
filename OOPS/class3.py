#oops Concepts
#1.Encapsulation- Wrapping up of data and functions into a single unit..eg class
#2.Inheritance- to acquire the property of one class to another class
#use - code reusability

#single inheritance
class A:
    def displayA(self):
        print('base class method')
class B(A):
    def displayB(self):
        print('Derive class method')

ob = B()
ob.displayA()
ob.displayB()
# class A:
#     def read(self):
#         self.x = int(input('enter a number:'))
#         self.y = int(input('enter a number:'))
#
# class B(A):
#     def sum(self):
#         print('Sum is :',self.x+self.y)
# ob = B()
# ob.read()
# ob.sum()

#  multilevel inheritance
# class A:
#     def read(self):
#         self.x = int(input('enter a number:'))
#         self.y = int(input('enter a number:'))
#
# class B(A):
#     def sum(self):
#         self.s=self.x+self.y
#         print('Sum is :',self.s)
# class C(B):
#     def Avg(self):
#         print('Sum is :',self.s/2)
# ob=C()
# ob.read()
# ob.sum()
# ob.Avg()

#Hierarchial Inheritance
# class A:
#     def read(self):
#         self.a = int(input('enter a number:'))
#         self.b = int(input('enter a number'))
# class B(A):
#     def sum(self):
#         self.s=self.a+self.b
#         print('sum is: ',(self.s))
# class C(A):
#     def Avg(self):
#         print('sum is:',(self.a+self.b)/2)
# class D(A):
#     def product(self):
#         print('product is:',(self.a*self.b))
#
# ob1 = B()
# ob1.read()
# ob1.sum()

# ob2 = C()
# ob2.read()
# ob2.Avg()

# ob3 = D()
# ob3.read()
# ob3.product()

# Multiple inheritance

# class A:
#     def Employee(self):
#         self.n = input('Enter the name:')
#         self.x = int(input('Enter the age:'))
# class B:
#     def readSalaryDetails(self):
#         self.des = input('enter the designation:')
#         self.sal = int(input('enter the salary:'))
# class C(A,B):
#     def EmployeeDetails(self):
#         print('{}:{},{}:{},{}:{},{}:{}'.format('Name is',self.n,'Age is,',self.x,'Designation is',self.des,'Salary is',self.sal))
#
# ob2 = C()
# ob2.Employee()
# ob2.readSalaryDetails()
# ob2.EmployeeDetails()

#3. polymorphism - one-in-many forms
# Two types -
#1. Compile Time (EG: Function Overloading)  early binding, static binding
#2. Runtime time(Eg: Function overrinding)   late binding ,dynamic binding















