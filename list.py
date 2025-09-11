name_list = ['Alp', 'Carter', 'Longyu', 'Samuel', 'Teo', 'Ryan', 'Oscar', 'George', 'Isaac', 'Kevin', 'Henry', 'Henry', 'Papa', 'Aidan', 'Thomas']
numbers=[]
high=-999
small=999
total=0
for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)
print("the third name is:",name_list[2])
print("The last seven names are:",name_list[-7:])
for i in range(5):
    number=int(input("enter a number"))
    numbers.append(number)
print(max(numbers),min(numbers),sum(numbers),sum(numbers)/5)
    
    
    
