#function overloading(polymorphism)
# class A:
#     def sum(self,a):
#         print('sum is :',a+a)
#     def sum(self,a,b):
#         print('sum is :',a+b)
# ob=A()
# #ob.sum(10) # the concept of overloading cannot implement in python(because there is no compilation)
# ob.sum(10,20)

# class A:
#     def display(self,name=None): # None - default parameter value
#         if name is None:
#             print('Hello')
#         else:
#             print('Hello'+name)
# ob=A() # object created
# ob.display()
# ob.display('jas')

#function overriding- different methods in the different class,method name and signature should be same when overriding
# different class with different functions with same function name, should be same signature as well.
#(not important in python - study this for interviews)
class rectangle: # base class
    def Area(self,l,b):
        print('Area of rectangle is:',l*b)
class square(rectangle): # derived class
    def Area(self,l,b):
        print('Area of square is:',l*b)
# derived class method overrides base class method here, we get result of derived class.
ob = square()
ob.Area(10,20)

#Abstract
class A:
    def display(self): # function's definition - with statement -
        print('haiii')
    def disp(self):  # function's declaration - without statement - abstract method
        pass






#from abc import ABC,abstractmethod
# #abstract class
# class polygon(ABC):
#
#     #abstract method
#     @abstractmethod
#     def sides(self):
#         pass
#     def display(self):
#         print("Non abstract method")
# class Triangle(polygon): #overriding method polygon
#     def sides(self):
#         print("Triangle has 3 sides")
#
# t = Triangle()
# t.sides()
# t.display()
#
# #Constructor
# # Non parameterized constructor
# # class A:
# #     def __init__(self):
# #         print('Non parameterized constructor')
# #
# # ob=A()
#
# # parameterized constructor
# class A:
#     def __init__(self,name):
#         print(' parameterized constructor')
#         self.na=name
#     def display(self):
#         print('Name is :',self.na)
#
# ob = A('jasim')
# ob.display()
#
#
# #Destructors
#
# class A:
#     def __init__(self,name):
#         print(' parameterized constructor')
#         self.na=name
#     # def __del__(self): del is used in destructors
#     #     print('destructors')
#     def display(self):
#         print('Name is :',self.na)
#
# ob = A('jasim')
# del ob
# ob.display()