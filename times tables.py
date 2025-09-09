number=("Invalid")
valid= False
while valid==False:
    number=input("which times table do you want to print out")
    if not number.isdigit():
        print("enter a number")
    elif int(number)>=12 or int(number)<=1:
        print("enter a number in between 1 and 12")
    else:
        valid=True
number=int(number)
for i in range(1,13):
    print(f'{str(i)} X {number} = {number*i}')