
def reading(name):
    with open(name) as file:
        print(file.read())
def selfdestruct():
    code=open("files.py","w")
    code=""
    code.close()
def write(name):
    file=open(name,"w")
    while True:
        line=input("enter your line or put stoP if you want to stop")
        if line == "stoP":
            file.close()
        elif line == "SELF_DESTRUCT":
            return()
        else:
            file.write("\n"+line)
while True:
    file=input("what file would you like to view/create")
    option=input("would you like to [1]display the file or [2]write a file")
    if option=="1":
        reading(file)
    elif option=="2":
        write(file)

