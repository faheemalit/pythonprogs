i=0
while(i<=2):

    print(i)
    i+=1
name=" "
def forprint(k):
    print("Your name is",k.title())
while(name!="q"):

    name=input("What is your name?\n")
    forprint(name)
    if(name=="ali"):
        break
    elif(name=="faheem"):
        break
    else:
        continue
        