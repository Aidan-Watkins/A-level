from math import *
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def perimiter(self):
        return 2*(self.length+self.width)
    def diagonal(self):
        return sqrt(self.length*self.length+self.width*self.width)

big=Rectangle(3,4)
print(big.area())
print(big.perimiter())
print(big.diagonal())
