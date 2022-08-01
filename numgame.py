def Numgame():    
    import random
    n = random.randint(20,31)
    bvalue = random.randint(1,101)
    if(bvalue>50):
        print("Number is greater than 50")
    else:
        print("Number is lesser than 50")  
    if(bvalue%2==0):
        print("Number is Even")
    else:
        print("Number is Odd")

    num = bvalue
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) ==0:
                flag = True
                break
    if flag or num==1:
        print("It is not a prime number")
    else:
        print("It is a prime number")
    while True:
        guess = int(input("Enter your guess "))
        if(guess==bvalue):
            print("Your Guess is correct")
            break
        elif(guess>bvalue):
            print("Numer is Smaller")
        elif(guess<bvalue):
            print("Number is Larger")
