#OOPS
#class-object
# class Emp:
#     def display(self):
#         print('function')
#
# obj = Emp()
# obj.display()
#
# class Emp:
#     x=100
#     def display(self):
#         print('function')
#
#
# obj = Emp()
# obj.display()
# print('value of x is',obj.x)


class Emp:
    x = 100

    def display(self):
        print('function')
    def sum(self):
    #def sum(self,a,b):
        print('sum is',30+40)
        #print('sum is',a+b)
    # def disp(): # we can call many function inside the class
    #     print('with out self parameter')
    def product(se,a,b):
        print('product is',a*b)

obj = Emp()
obj.display()
obj.sum()
#obj.sum(30,40)
print('value of x is', obj.x)
# ob=Emp
# ob.disp()



