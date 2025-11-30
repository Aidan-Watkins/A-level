def hash(item):
    sum=0
    for char in item:
        sum=sum+ord(char) **2
    return sum%523
memory=[]
for i in range(523):
    memory.append("-1")
memory[hash("PEN")]="PLUME"
memory[hash("CAT")]="CHAT"
memory[hash("NOW")]="MAINTENANT"
a="N"
while a=="N":
    print(memory[hash(input("which english word do you want to translate"))])
    a=input("do you want to exit Y or N").upper()
