from random import *
highscore=9999
print("your guess will be judged with the correct first then correct but in the wrong space for example 1,0 means 1 in the right space and none right but in the wrong space")
while True:
    length=int(input("how may digits should the number be"))
    guesses=0
    #target generation
    target=[]
    for i in range(length):
        target.append(str(randint(0,9)))
    #print(target)
    win=False
    def guess():
        number="a"
        #continually asks for guess untill it is the right format
        while len(number)!=length or not number.isdigit():
            number=str(input("what is your guess"))
            lstguess=[]
        for digit in number:
            lstguess.append(digit)
        return(lstguess)
    def correct(target,guess):
        #print(guess)
        global win
        correctspace=0
        correctwrong=0
        temptarget=target.copy()
        #print(temptarget)
        #print(target)
        for i in range(length):
            if temptarget[i]==guess[i]:
                correctspace+=1
                guess[i]=-1
                temptarget[i]=-2
        #print(guess)
        for i in range(length):
            for y in range(length):
                if guess[i]==temptarget[y]:
                    correctwrong+=1
                    guess[i]=-1
                    temptarget[y]=-2
        #print(correctspace)
        if correctspace==length:
            win= True
        return(correctspace,correctwrong)
    while not win:
        guesses+=1
        print(correct(target,guess()))
    print("you win in",guesses)
    if guesses<highscore:
        highscore= guesses
        print("New Highscore!")
