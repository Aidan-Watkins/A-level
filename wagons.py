class Wagon:
    def __init__(self,name):#,doors,owner,weight):
        #self.door=doors
        #self.owner=owner
        #self.weight=weight
        self._name=name
    def __str__(self):
        return(self._name)
class Closedwagon(Wagon):
    def __init__(self,name):
        super().__init__(name)
class Openwagon(Wagon):
    def __init__(self,name):
        super().__init__(name)
class Sliding:
    def __init__(self):
        self._top=-1
        self._wagon_array=[None]*30
    def push(self,wagon):
        self._top+=1
        self._wagon_array[self._top]=wagon
    def pop(self):
        temp=self._wagon_array[self._top]
        self._top-=1
        return temp
class yard(Sliding):
    def __init__(self,slidings):
        self._slidings=Sliding*slidings
    def push(self,sliding):
        self._slidings[sliding].push
    
w1=Closedwagon("Thomas")
w2=Wagon("Henry")
w3=Wagon("Diesl")
w4=Wagon("Teo")
slide = Sliding()
yard1=yard(5)
yard1.push(w1)
yard1.push(w3)
yard1.push(w2)
print(yard.pop())
print(slide.pop())
print(slide.pop())