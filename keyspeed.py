import keyboard
import random
import time
from threading import Lock, Thread
h = True
def countdown(lock):
    global h
    with lock:
        for i in range(10,0,-1):
            i = str(i)
            if len(i)==1:
                i = "0"+i
            print(i,end="\r")
            time.sleep(1)
    h = False
def key_cheak():
    global score
    score = 0
    f = open('keys.txt','r')
    read = f.readlines()
    read = [x.replace('\n','') for x in read]
    while h:
        a = random.choice(read)
        print("Press Key ",a) 
        while True:
            if keyboard.is_pressed(a):
                score+=1
                break
    f.close()
if __name__ == 'keyspeed':
    s = input("Enter S to begin ")
    if s=="s"or"S":
        lock = Lock()
        t1 = Thread(target=countdown,args=(lock,))
        t2 = Thread(target=key_cheak,args=())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("Your Score is ",score)