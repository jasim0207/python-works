#super() - function used to give access to the method of a parent class
#          returns a temporary object of a parent class when used

# class rectangle:
#     pass
# class square(rectangle):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#
# class cube(rectangle):
#     def __init__(self,length,width,height):
#         self.length = length
#         self.width = width
#         self.height = height
#
# sq = square(3,3)
# cb = cube(3,3,3)

class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class square(rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width

class cube(rectangle):
    def __init__(self,length,width,height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        return self.length*self.width*self.height
sq = square(3,3)
cb = cube(3,3,3)

print(sq.area())
print(cb.volume())
