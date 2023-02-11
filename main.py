# imported modules
import importlib
from itertools import count
import numgame as na
import wordxe as wa
import MemoryG as ma
import logris as lo
import Word_guess as wg
import Hangman as hg
def getShowarr(blist):
    l = []
    for i in range(0,len(blist)):
        if(i != 3):
            a = blist[i].split(",")
            l.append(list(map(int, a)))
    return l
def updateArray(lis,ind):
    list_string = map(str, lis)
    blist[ind] = ",".join(list_string)
def getArray(f,num):
    x = f[num].split(",")
    x = [int(i) for i in x]
    return x
def rep():
    global cont,exe
    n1 = input("Want to continue playing this game (y/n)")
    if n1=="n":
        n2 = input("Do you want exit y/n ")
        if n2=="y":
            cont = 0
        else:
            exe=0
cont = 1
# imported text files
f1 = open('Abc.txt','r')
f2 = open('numgame.txt','r')
r1 = f1.read()
s1 = r1.split("\n")
r2 = f2.read()
print("Welcome to GLAB , Your Ultimate Destination For Puzzle Games")
print("We Can offer you common as well as exclusive games")
print("To Play as a new user you can register or as a new user you can login ")
lo.logr()
d = lo.getSt()
blist = d.split("/")
print(r1)
while cont==1:
    n = input("Enter the Game No. or Enter n to exit: ")
    exe = 1
    if n=="1":
        ee = 1
        print(r2,end="\n")
        while ee==1:
            na.Numgame(getArray(blist,int(n)-1))
            updateArray(na.getBack(),int(n)-1)
            rep()
            if exe==0:
                break
            if cont==0:
                break
    if cont==0:
        break
    if n=="2":
        ec=1
        print("You have Chosen 'Jumble Words'")
        print("Rearrange the following words to get to the desired sentence:")
        while ec==1:
            wa.jumble(getArray(blist,int(n)-1))
            updateArray(wa.getBack(),int(n)-1)
            rep()
            if exe==0:
                break
            if cont==0:
                break
    if n=="3":
        er=1
        print("You have Chosen 'Memory Word Game'")
        print("5 Pairs will be shown for some time one of which will be asked(You Have 2 attempts)")
        while er==1:
            ma.Memory(getArray(blist,int(n)-1))
            updateArray(ma.getBack(),int(n)-1)
            rep()
            if exe==0:
                break
            if cont==0:
                break
    if n == "4":
        et = 1
        print("You have Chosen 'Key Speed Check'")
        print("You get 10 second In Which You Have to Press Maximum number of the given keys")
        d=0
        while et==1:
            if d==0:
                import keyspeed
                d+=1    
            elif(d==1):
                importlib.reload(keyspeed)
            rep()
            if exe==0:
                break
            if cont==0:
                break
    if n == "5":
        ew = 1
        print("You have Chosen 'Hard Wordle")
        print("Instructions : Word Should have 5 Letters \n Red Colour means Letter is not in the Word \n Yellow Colour means Letter is in the Word but Is in Wrong Place \n Green Colour means Letter is in Word and Is at the Right Place")
        while ew == 1:
            wg.Mywordle(getArray(blist,int(n)-1))
            updateArray(wg.getBack(),int(n)-1)
            rep()
            if exe==0:
                break
            if cont==0:
                break
    if n =="6":
        eh = 1
        print("You have Chosen 'Hangman'")
        print("You have to find the word by entering a Character before the man is hanged")
        while eh == 1:
            hg.hang(getArray(blist,int(n)-1))
            updateArray(hg.getBack(),int(n)-1)
            rep()
            if exe==0:
                break
            if cont==0:
                break
    if n.lower()=="s":
        print("Your Stats are :")
        lo.showStats(getShowarr( blist))
    d = "/".join(blist)
    lo.updateStats(d)
    if cont==0:
        break
    if n=="n":
        break