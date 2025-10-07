from math import *
class rectangle:
    def _init_(self,length,width):
        self._length = length
        self._width = width
    def area(self):
        return(self._length*self._width)
    def perimiter(self):
        return(2*(self._length+self._width))
    def diagonal(self):
        return(sqrt(self._length*self._length+self._width*self._width))

big=rectangle
big._init_(big,100,50)
print(rectangle.area(big))
print(rectangle.perimiter(big))
print(rectangle.diagonal(big))
