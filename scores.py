
name_list =  ['Ryansh', 'Oliver', 'Edward', 'Daniel', 'Alex', 'Ares', 'Thomas', 'Andy', 'Charlie', 'Ryan', 'Lucas']
scores_list = [[] for i in name_list]           # Create a lists of empty lists

#print(sum(scores_list[name_index])/len(scores_list[name_index]))
#print(f"the average for{name}, is {scores_list[name_index]}")
def addscore(name_index,new_score):
   
    scores_list[name_index].append(new_score)    # Append the new score to the list in the relevant location within scores
def displayscore(name_index,name):
    print(f"the average for{name}, is {sum(scores_list[name_index])/len(scores_list[name_index])}")
    print(scores_list[name_index])
exit=False
def menu():
    option=input("enter 1 if you want to display average and scores for a person 2 for adding score or 3 to exit")
    name = input("Enter name: ")
    name_index = name_list.index(name)
    if option=="1":
        displayscore(name_index,name)
    if option=="2":
        new_score = int(input("Enter score: ")) 
        addscore(name_index,new_score)
    if option=="3":
        exit=True
while exit==False:
    menu()
