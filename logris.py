import pandas as pd
def sqlcon():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="GLab"
  )
  mycur = mydb.cursor()
  def save():
    mydb.commit()
  return mycur,mydb
def logr():
  import getpass
  global j,id
  mycur,mydb = sqlcon()
  kk1 = 0
  while(kk1==0):
    nn = input("Enter 1 to Register or 2 to Login ")
    if nn=="1":
      n = input("Enter your Name: ")
      s = input("Your Password: ")
      k=0
      mycur.execute("SELECT * FROM Users")
      r = mycur.fetchall()
      if r==[]:
          k=1
      else:
        a = list(r[-1])
        k = a[-2]+1
      print("Your UID is "+str(k))
      mycur.execute("INSERT into Users Values('{}','{}',{},'0,0,0/0,0,0/0,0,0/0,0,0/0,0,0/0,0,0')". format(n,s,k))
    elif nn=="2":
      n = int(input("Enter your UID: "))
      s = getpass.getpass("Your Password: ")
      mycur.execute("SELECT * FROM Users")
      r = mycur.fetchall()
      i = 0
      while i<len(r):
        a  = list(r[i])
        id =a[2]
        if a[1]==s and (a[2]==n or f'{a[2]}'==n):
          kk1 = 1
          j = a[3]
          print("You have logined as "+a[0])
          break
        elif a[1]!=s and a[2]==n:
          print("Your Password is Wrong")
          break
        else:
          i+=1
      else:
        print("You are not registered try again")
        break
    mydb.commit()
def getSt():
  return j
def updateStats(rsa):
  global j
  j = rsa
  mycur,mydb = sqlcon()
  mycur.execute("Update Users SET Stats ='{}' Where uid= {}".format(rsa,id))
  mydb.commit()
def showStats(blist):
  df = pd.DataFrame(blist,index=["Numgame","JumbleWords","Memory Game","Wordle","Hangman"],columns=["Games","Wins","Loses"])
  print(df)