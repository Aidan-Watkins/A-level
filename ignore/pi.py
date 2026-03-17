import random
incirc=0
trials=10000000
for i in range(trials):
    x=random.random()
    y=random.random()
    if x**2+y**2<1:
        incirc+=1
print((incirc/trials)*4)

pi=0
for i in range(10000000):
    if i%2==0:
        pi+=1/(2*i+1)
    else:
        pi-=1/(2*i+1)
pi*=4
print(pi)