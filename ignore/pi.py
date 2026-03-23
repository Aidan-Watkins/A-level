import random
import math
import decimal
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
trials=30
pi=0
average=0
for i in range(trials):
    heads=0
    flips=0
    while (flips==0 or heads/flips<=0.5) and flips <1000000:
        if random.randint(0,1)==1:
            heads+=1
        flips+=1
    if flips>1000000:
        average+=0.5
    else:
        average+=heads/flips
pi=4*average/trials
print(pi)
decimal.getcontext().prec=100
trials=15
pi=decimal.Decimal(0)
average=0
for i in range(trials):
    pi+=decimal.Decimal(((-1)**i)*math.factorial(6*i)*(545140134*i+13591409))/decimal.Decimal(math.factorial(3*i)*math.factorial(i)**3*(640320)**(3*i+3/2))
pi*=12
print(1/pi)
