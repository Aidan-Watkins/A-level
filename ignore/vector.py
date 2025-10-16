import math
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def mag(self):
        return math.sqrt(self.x**2+self.y**2)
    
    def angle(self):
        return math.degrees(math.atan(self.y/self.x))
    
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)
    
    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        return Vector(x,y)
    def __str__(self):
        return str(self.x)+","+str(self.y)

def test():
    vec1=Vector(3,4)
    vec2=Vector(4,5)
    if vec1.mag()==5:
        print("test passed")
    else:
        print("test failed")


    print(vec1.angle())
    print(vec2.angle())
    print(vec1)
    print(vec1+vec2)
    print(vec1-vec2)
    print(vec2-vec1)

test()