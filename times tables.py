number=("Invalid")
while not number.isdigit():
    number=input("which times table do you want to print out")
number=int(number)
for i in range(1,12):
    print(str(i)+"X"+str(number)+"="+str(number*i))