# class Emp:
#     def read(self,a,b):
#         self.x=a  # current variable self.x, self.x = a , a is passing and assigning to variable self.x,
#         self.y=b  #
#     def sum(self):
#         print('sum is :',self.x+self.y)
#     def product(c):
#         print('product is:',c.x*c.y)
#
# obj=Emp()
# obj.read(10,20)
# obj.sum()
# obj.product()


class Emp:
    def read(self,a,b):
        self.a=a  # current variable self.x, self.a = a , a is passing and assigning to variable self.a,
        self.b=b  #
    def sum(self):
        print('sum is :',self.a+self.b)
    def product(c):
        print('product is:',c.a*c.b)

obj=Emp()
obj.read(10,20)
obj.sum()
obj.product()
