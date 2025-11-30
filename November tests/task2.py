word1=input("Enter a first word ").upper()
word2=input("Enter a second word ").upper()
letters=[]
works=True
#splits up the characters from the second word into a list
for char in word2:
    letters.append(char)
#iterates through all of the characters in the first word with setting the found for that letter false each time 
for char in word1:
    found=False
    for item in range(len(letters)):
        if letters[item]==char:
            letters[item]=-1
            found=True
            char=0
    if not found:
        works=False
#prints if it is possible to make the first word from the second word
if works:
    print("it is possible to make the first word from the second word")
else:
    print("it is not possible to make the first word from the second word")
        
