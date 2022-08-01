def hang():    
    from Hangpics import pics
    import random
    import re
    def ndel(l,l1):
            for i in  l:
                a = i.replace("\n","")
                l1.append(a)
    f = open('Hangwords.txt','r')
    g = f.readlines()
    h = []
    ha = 0
    ndel(g,h)
    A = random.choice(h)
    A = A.upper()
    I = ""
    for i in A:
        I+="_"
    for j in I:
        print(j,end=" ")
    print()
    while not I==A:
        while ha<6:
            if not I==A:
                g = input("Enter a Letter: ")
                g  = g.upper()
                if g in A:
                    indices = [i.start() for i in re.finditer(g, A)]
                    for l in indices:
                        I = I[:l]+g+I[l+1:]
                    print("Given Letter is in the Word")
                    print("Your Current State")
                    for j in I:
                        print(j,end=" ")
                    print(pics[ha])
                else:
                    ha+=1
                    print("Given Letter is not in the Word")
                    print("Your Current State")
                    for j in I:
                        print(j,end=" ")
                    print(pics[ha])
            else:
                for j in I:
                    print(j,end=" ")
                print()
                print("You Have Found Out The Word")
                break
        else:
            print("You are out of Guesses")
            print("The Correct Word is "+A)
            print("Better Luck Next Time")
            break