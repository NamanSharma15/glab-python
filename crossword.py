import math
def HBorder(text,vertical = 0,joint_index=[0,False]):
    letters = [i for i in text]
    diff=-1
    for i in range(1,math.ceil(len(letters)/2)):
        diff+=1
    res = []
    f=0
    for i in letters:
        if i==" ":
            f+=1
    if " " in letters:
        letters.remove(" ")
    width = len(letters)*3+int(len(letters)/2)+diff+1
    res.append('┌' + '─' * width + '┐')
    for s in letters:
        res.append(s + ' │')
    res.append('└' + '─' * width + '┘')
    print("    "*f,end="")
    print(res[0])
    print("    "*f,end="")
    print("│ ",end="")
    for i in range(1,len(res)-1):
        print(res[i],end=" ")
    print()
    print("    "*f,end="")
    print(res[-1])
def VBorder(text):
    letters = [i for i in text]
    res = []
    for s in letters[0:-1]:
        res.append("│ "+s + ' │')
        res.append('│' +""+ '─' * 3 + '│')
    res.append("│ "+letters[-1] + ' │')
    res.append('└' +""+ '─' * 3 + '┘')
    print(res[0])
    for i in range(1,len(res)-1):
        print(res[i],end="\n")
    print(res[-1])
HBorder("ALIVE")
HBorder(" I")
