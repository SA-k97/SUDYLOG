import random


playground=["-","-","-"
           ,"-","-","-"
           ,"-","-","-"]

Player="X"
Winner= None
gameRun=True

def printPlayGround(playground):
    print(playground[0]+"|"+ playground[1]+"|"+ playground[2])
    print("-----")
    print(playground[3]+"|"+ playground[4]+"|"+ playground[5])
    print("-----")
    print(playground[6]+"|"+ playground[7]+"|"+ playground[8])

def playerInput(playground):
    inp= int(input("enter a number between 1-9: "))
    if inp>=1 and inp<=9 and playground[inp-1]=="-":
       playground[inp-1]= Player
    else:
        print("this place doesn’t exist plese choose a number between 1-9")


def theRow(playground):
    global winner
    if playground[0]==playground[1]==playground[2] and playground[1]!="-":
        winner= playground[0]
        return True
    elif playground[3]==playground[4]==playground[5] and playground[3]!="-": 
        winner= playground[3]
        return True
    elif playground[6]==playground[7]==playground[8] and playground[6]!="-":     
        winner= playground[6]
        return True
def theColumn(playground):
    global winner
    if playground[0]==playground[3]==playground[6] and playground[0]!="-":
        winner= playground[0]
        return True
    elif playground[1]==playground[4]==playground[7] and playground[1]!="-": 
        winner= playground[1]
        return True
    elif playground[2]==playground[5]== playground[8] and playground[2]!="-":     
        winner= playground[2]
        return True    

def theDiag(playground):
    global winner
    if playground[0]== playground[4]== playground[8] and playground[0]!="-":
        winner= playground[0]
        return True
    elif playground[2]== playground[4]== playground[6] and playground[2]!="-": 
        winner= playground[2]
        return True 

def ifTie(playground):
    global gameRun
    if "-" not in playground:
        printPlayGround(playground)
        print("it's a Tie! He He ")
        gameRunning=False
def ifWin():
    global gameRunning
    if theDiag(playground) or theRow(playground) or theColumn(playground):
        print(f"okay you won {winner} ‘clapping audience’") 
        printPlayGround(playground)
        gameRunning=False
def otherPlayer():
    global Player
    if Player=="X":
        Player="O"  
    else:
        Player="X"  
def Bestie(playground):
    while Player== "O":
        position= random.randint(0,8)
        if playground[position]=="-":
            playground[position]="O"
            otherPlayer()  
while gameRun:
    printPlayGround(playground)
    playerInput(playground)
    ifWin()
    ifTie(playground)
    otherPlayer()
    Bestie(playground)
    ifWin()
    ifTie(playground)


    
