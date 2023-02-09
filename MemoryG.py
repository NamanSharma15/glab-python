def Memory(slist):
    global x
    import time,random
    slist[0]+=1
    def limP(b):
        print (b,end="\r")
        time.sleep(3.5)
        c = "//////////////////\\\\\//////////\\\/////\\/"
        print (c,end ="\n")
        time.sleep(2)
    def ndel(l,l1):
        for i in  l:
            a = i.replace("\n","")
            l1.append(a)
    kkk = input("Enter S to begin")
    if (kkk=="S"or"s"):
        f1 = open('People.txt','r')
        f2 = open('Fruits.txt','r')
        lx = f1.readlines()
        kx = f2.readlines()
        L = []
        K = []
        ndel(lx,L)
        ndel(kx,K)
        num = []
        while len(num)<5:
            r1 = random.randint(0,len(L)-1)
            if r1 not in num:
                num.append(r1)
        for i in num:
            limP(L[i]+":"+K[i])
        r = random.randint(0,4)
        c = num[r]
        ip = 0 
        for i in range(2):
            n = input("Enter The Faviourate Fruit of a "+L[c]+" : ")
            if n==K[c]:
                print("Well Done")
                slist[1]+=1
                break
            elif i<1:
                print("try again \n")
            i+=1
        if i>1:
            print("Correct Fruit For "+L[c]+" is "+K[c])
            slist[2]+=1
    x = slist
def getBack():
    return x