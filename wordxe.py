def jumble():
    import random
    f1 = open('WordH.txt','r')
    s = f1.readlines()
    num = len(s)
    b = random.randint(0,len(s)-1)
    sentence  = s[b]
    words = sentence.split(" ")
    words1 = []
    for i in words:
        if("\n" in i):
            s = i.replace(".\n","")
            words1.append(s)
        else:
            s = i
            words1.append(s)
    l = []
    for i in range(len(words1)):
        l.append(i)
    for j in range(len(l)):
        kk = len(words1)- 1
        ab = random.randint(0,kk)
        x = words1[ab]
        print(x,end=" ")
        words1.pop(ab)
        kk-=1
    print()
    i = 0
    for i in range(5):
        guess = input("Enter the Correct Sentence: ")
        if guess==sentence.replace("\n",""):
            print("Correct Sentence")
            break
        elif(guess!=sentence.replace("\n","") and i<4):
            print("Try again")
        else:
            print("Desired Sentence is "+sentence)
            print("Better Luck Next Time")
