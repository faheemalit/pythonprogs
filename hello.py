c="yes"
while(c=="yes"):
    x=input("Which Table?")
    p=int(x)

    for k in range(10):
        m=p*k
        print(k,"X",p,"=",m)
    c=input("Next? (Yes/No)")