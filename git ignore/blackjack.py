from random import *
from math import *
money=2000
bet=0
total=[]
dealertotal=[]
stop=False
def totaltoprint(total):
    aces=0
    number=0
    for item in total:
        if item==1:
            aces+=1
        else:
            number+=item
    for i in range(aces):
        if number+aces-i>11:
            number+=1
        else:
            number+=11
    return(number)
def roll():
    number=randint(1,14)
    if number>9:
        return(10)
    else:
        return(number)
while money >0:
    print("")
    print("you have",money)
    first=True
    lose=True
    bet=-1
    while bet > money or bet <1:
        bet=(input("how much are you betting"))
        if bet.isdigit():
            bet=int(bet)
        else:
            bet=-1
    money-=bet
    dealertotal.append(roll())
    print("the dealer drew a",totaltoprint(dealertotal),dealertotal)
    total.append(roll())
    total.append(roll())
    print("with you two draws you have",totaltoprint(total),total)
    while stop==False and totaltoprint(total)<21:
        if bet<=money and first==True:
            stopper=input("would you like to hit again [y],[N] or [D]ouble").upper().strip()
        else:
            stopper=input("would you like to hit again [y] or [N]").upper().strip()
        if stopper=="D" and bet<=money and first==True:
            money-=bet
            bet*=2
            stop=True
            print("doubled to",bet)
        if stopper=="N":
            stop=True
        else :
            total.append(roll())
            print("your total is now",totaltoprint(total),total)
        first=False
    if totaltoprint(total)>21:
        lose=True
    else:
        while totaltoprint(dealertotal)<17:
            dealertotal.append(roll())
        print("the dealer got",totaltoprint(dealertotal),dealertotal)
        if totaltoprint(dealertotal)<=21:
            if totaltoprint(dealertotal)>totaltoprint(total):
                lose=True
            elif totaltoprint(dealertotal)==totaltoprint(total):
                money+=bet
               
            else:
                lose=False
                if len(total)==2 and totaltoprint(total)==21:
                    money+=floor(bet/2)
                    print("Blackjack Yayy!!!")
        else:
            lose=False
            if len(total)==2 and totaltoprint(total)==21:
                    money+=floor(bet/2)
                    print("Blackjack Yayy!!!")
        if lose==False:
                  money+=bet*2
    total=[]
    stop=False
    dealertotal=[]
