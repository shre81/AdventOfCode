from cProfile import run
import os

#f = open("input-2-test", "r")
f = open("input-2", "r")

playDct = {"A":1, "B": 2, "C": 3}
myDct = {"X": 1, "Y": 2, "Z": 3}
scrDct = {"W":6, "D": 3, "L":0}

def calcWinner(ply, mine):
    if (playDct[ply] == myDct[mine]):
        scr = "D"
    elif ((myDct[mine] - playDct[ply]) == 1) or ((myDct[mine] - playDct[ply]) == -2):
        scr = "W"
    else:
        scr = "L"
    return scr

bigLst = []

for items in f:
    bigLst.append(items)

runScr = 0

for games in bigLst:
    gamScr = scrDct[calcWinner(games[0], games[2])] + myDct[games[2]]
    runScr = runScr + gamScr

# Part - 2

actDct = {"X": "L", "Y": "D", "Z": "W"}
rvDct = {v: k for k,v in myDct.items()}

def calcGame(ply, my):
    myPlay = 'R'
    if actDct[my] == "D":
        myPlay = rvDct[playDct[ply]]
    elif actDct[my] == "W":
        if ply == "C":
            myPlay = "X"
        else:
            myPlay = rvDct[playDct[ply] + 1]
    else:
        if ply == "A":
            myPlay = "Z"
        else:
            myPlay = rvDct[playDct[ply] - 1]
    
    totScr = myDct[myPlay] + scrDct[actDct[my]]
    
    return totScr

#print (bigLst[0][0], bigLst[0][2])

run2Scr = 0

for games in bigLst:
    run2Scr = run2Scr + calcGame(games[0], games[2])

print (run2Scr)