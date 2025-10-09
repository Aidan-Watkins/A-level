"""filename="sampledata.csv"
with open(filename,'r') as csv_file:
    for line in csv_file:
        data = line.strip("ï»¿").strip().split(",")
        name=data[0]
        score=data[1]
        exam1=data[2]
        exam2=data[3]
        print(name,score,exam1,exam2)"""
name=["a","b","c"]
score=["1","2","3"]
age=["10","11","12"]
with open("csvfile.txt","w")as file:
    for i in range(3):
        line=str(f"{name[i]},{score[i]},{age[i]}\n")
        file.write(str(line))