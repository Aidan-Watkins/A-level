from datetime import datetime
tasks=[]

def addtask(name,due,sub,done):
    global tasks
    tasks.append([name,due,sub,done])
    tasks[-1][1]= datetime.strptime(tasks[-1][1],"%Y-%m-%d")
    tasks = sorted(tasks, key=lambda x: x[1])
def displaytasks():
    for item in tasks:
        for data in item:
            print(str(data),end=" ")
        print("")
def nexttask():
    print("Your next task is")
    print(tasks[0])
    print("your net task that is not done is:")
    for i in range(len(tasks)):
        if tasks[i][3]=="N":
            print(tasks[i])
            break
def complete(name):
    for i in range(len(tasks)):
        if tasks[i][0]==name:
            tasks[i][3]="Y"


addtask("Math HW", "2025-09-15", "Math","Y")
addtask("Physics equasions", "2025-09-20", "Science","N")
addtask("Chemistry HW", "2025-09-10", "Chemistry", "N")
exit=False
while exit==False:
    choice=input("""What would you like to do
1)  add a task
2)  display all of your tasks
3)  display next tasks
4)  mark a task a done
5)  exit
""")
    if choice=="1":
        name=input("what is your new task called")
        due=input("when is that task due")
        sub=input("what subject is the task for")
        done=input("is it done [Y]/[N]").upper().strip()
        addtask(name,due,sub,done)
    elif choice=="2":
        displaytasks()
    elif choice=="3":
        nexttask()
    elif choice=="4":
        name=input("what is your completed task called")
        complete(name)
    elif choice=="5":
        exit=True