import math
from termcolor import colored
import os
import time
import random
class Player:
    def __init__(self,color):
        self.pos = 1
        self.color = color
def diceRoll():
    num = random.randint(1,6)
    return num
def playerAtt(ply):
    l = []
    for i in ply:
        l.append({"point":getval(i.pos),"color":i.color})
    return l
def movState(alp):
    a1 = []
    a2 = []
    it = 0
    for i in alp:
        val = list(i.values())
        a1.append(val[0])
        a2.append(val[1])
    return [a1,a2]
def playerCol(pla,s:str,col,bcol=0):
    f = 0
    g = 0
    s1 = s
    if(bcol==0):
        if(s1==pla[0]):
            s = colored(s[0],on_color="on_"+col[0]) + s[1:]
        if(s1==pla[1]):
            s  = s[:-1] + colored(s[-1],on_color="on_"+col[1])
    elif(bcol==1):
        if(s1==pla[0]):
            s = colored(s[0],color="white",on_color="on_"+col[0]) + colored(s[1:],on_color='on_red')
        if(s1==pla[1]):
            s  = colored(s[:-1],on_color='on_red') + colored(s[-1],on_color="on_"+col[1])
    else:
        if(s1==pla[0]):
            s = colored(s[0],color="white",on_color="on_"+col[0]) + colored(s[1:],on_color='on_green')
        if(s1==pla[1]):
            s  = colored(s[:-1],on_color='on_green') + colored(s[-1],on_color="on_"+col[1])
    
    return s
def HBorder(text,sp_block:list,last=False):
    gc = sp_block[0]["color"]
    gp = list(map(getval,sp_block[0]["points"]))
    rc = sp_block[1]["color"]
    rp = list(map(getval,sp_block[1]["points"]))
    players = playerAtt(sp_block[2])
    state = movState(players)
    letters = text.split(" ")
    diff=-1
    for i in range(1,math.ceil(len(letters)/2)):
        diff+=1
    width = len(letters)*5+int(len(letters)/2)+diff+1
    res = []
    # res.append('│' + '─' * width + '│')
    for s in letters:
        s1 = s
        if(s in gp and s1 not in state[0]):
            s = colored(s,on_color="on_"+gc)
        elif(s in rp and s1 not in state[0]):
            s = colored(s,on_color="on_"+rc)
        elif(s1 in state[0] and s not in rp and s not in gp ):
            s = playerCol(state[0],s,state[1])
        elif(s1 in state[0] and s in rp):
            s= playerCol(state[0],s,state[1],bcol=1)
        else:
            s= playerCol(state[0],s,state[1],bcol=2)
        res.append(s + ' │')
    if last:
        res.append('└' + '─' * width + '┘')
    else:
        res.append('│' + '─' * width + '│')
    print("│ ",end="")
    for i in range(0,len(res)-1):
        print(res[i],end=" ")
    print()
    print(res[-1])
def getval(i:int):
    i = str(i)
    if( len(i) == 1):
        i="00"+i
    elif(len(i)==2):
        i="0"+i
    return i
def getUp(pla,pos,arr):
    a = random.choice(arr)
    if(pos == max(arr)):
        pla.pos = pos
    else:
        while a<=pos:
            a = random.choice(arr)
    pla.pos = a
def getDown(pla,pos,arr):
    a = random.choice(arr)
    if(pos ==min(arr)):
        pla.pos = pos
    else:
        while a>=pos:
            a = random.choice(arr)
    pla.pos = a
def boardState(red_p,green_p,players):
    print("┌───────────────────────────────────────────────────────────┐")
    s  = []
    d  = 0 
    spla = [green_p,red_p,players]
    for i in range(100,0,-1):
        if(len(s)<10):
            s.append(getval(i))
        else:
            if(d%2==0):
                HBorder(" ".join(s),spla)
            else:
                s.reverse()
                HBorder(" ".join(s),spla)
            s=[getval(i)]
            d+=1
        if(i==1):
            s.reverse()
            HBorder(" ".join(s),spla,last=True)
redPoints = {"color":"red","points":[99,45,32,93,95,56,77,22,65]}
greenPoints  = {"color":"green","points":[10,7,21,41,91,66,80,39]}
Players = []
colors = ["yellow", "blue", "magenta", "cyan", "white"]
for i in range(2):
    p = Player(color=colors[i])
    Players.append(p)
print("Welcome to Snake and Ladders - Random Version ")
s = input("Enter s to start")
d  = 0
while True:
    os.system('cls')
    print(f"Player {(d%2)+1} turn")
    boardState(redPoints,greenPoints,Players)
    e = input("Enter a to roll the dice: ")
    num = diceRoll()
    print("The roll is :",num)
    time.sleep(3)
    if(Players[d%2].pos+num<100):
        for i in range(0,num):
            os.system('cls')
            print(f"Player {(d%2)+1} turn")
            Players[d%2].pos+=1
            boardState(redPoints,greenPoints,Players)
            time.sleep(0.5)
        if(Players[d%2].pos in greenPoints["points"]):
            getUp(Players[d%2],Players[d%2].pos,greenPoints["points"])
        elif((Players[d%2].pos in redPoints["points"])):
            getDown(Players[d%2],Players[d%2].pos,redPoints["points"])
    elif(Players[d%2].pos+num==100):
        for i in range(0,num):
            os.system('cls')
            print(f"Player {(d%2)+1} turn")
            Players[d%2].pos+=1
            boardState(redPoints,greenPoints,Players)
            time.sleep(0.5)
        winner = d%2+1
        break
    d+=1
os.system('cls')
print("Winner is Player ",winner)
boardState(redPoints,greenPoints,Players)
time.sleep(5)