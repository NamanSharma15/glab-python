def logr():
  import mysql.connector
  import getpass
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="GLab"
  )
  mycur = mydb.cursor()
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
        k = a[-1]+1
      print("Your UID is "+str(k))
      mycur.execute("INSERT into Users Values('{}','{}',{})". format(n,s,k))
    elif nn=="2":
      n = int(input("Enter your UID: "))
      s = getpass.getpass("Your Password: ")
      mycur.execute("SELECT * FROM Users")
      r = mycur.fetchall()
      for i in r:
        a  = list(i)
        if a[1]==s and a[2]==n:
              kk1 = 1
              print("You have logined as "+a[0])
              break
        elif a[1]!=s and a[2]==n:
          print("Your Password is Wrong")
          break
        else:
          print("You are not registered try again")
          break
  mydb.commit()