def Mywordle(slist):
    global x    
    from termcolor import colored
    import random
    def ndel(l,l1):
            for i in  l:
                a = i.replace("\n","")
                l1.append(a)
    h = True
    f = open('wordlist.txt','r')
    g = f.readlines()
    slist[0]+=1
    h = []
    ndel(g,h)
    r = random.randint(0,len(h)-1)
    A = h[r]
    A=A.upper()
    l1 = [i for i in A]
    P=0
    while P<6:
        Inp = input("Enter The Word: ")
        Inp = Inp.upper()
        if len(Inp)==5:
            if not Inp==A and P<5:
                l = [i for i in Inp]
                for i in l:
                    if i not in l1:
                        print(colored(i,'white','on_red'),end=" ")
                    elif i in l1 and not l.index(i)==l1.index(i):
                        print(colored(i,'white','on_yellow'),end=" ")
                    elif l.index(i)==l1.index(i):
                        print(colored(i,'white','on_green'),end=" ")
                print()
            elif Inp==A:
                print("Correct Guess")
                print(colored(Inp,'white','on_green'))
                slist[1]+=1
                break
            else:
                l = [i for i in Inp]
                for i in l:
                    if i not in l1:
                        print(colored(i,'white','on_red'),end=" ")
                    elif i in l1 and not l.index(i)==l1.index(i):
                        print(colored(i,'white','on_yellow'),end=" ")
                    elif l.index(i)==l1.index(i):
                        print(colored(i,'white','on_green'),end=" ")
                print()
                print("You are Out of Guesses try again")
                print("Correct Word is "+A)
                slist[2]+=1
                break
            P+=1
        else:
            print("Enter a Five Lettered Word Instead")
    x = slist
def getBack():
    return x