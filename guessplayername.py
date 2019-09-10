#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 06:41:11 2019

@author: faheem
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:07:01 2019

@author: faheem
"""
import random

def choose():
    words=["beckham","zidane","guti","carlos","messi","ronaldo","ronaldinho","raul","figo","ballack","henry","robben"]
    pick=random.choice(words)
    return pick

def create_qn(word):
    n=len(word)
    letters=list(word)
    temp=[]
    for i in range(n):
        if(letters[i]==" "):
            temp.append(' ')
        else:
            temp.append('-')
    qn="".join(str(x) for  x  in temp)
    return qn

def is_present(letter,movie):
    k=0
    letters=list(movie)
    for i in range(len(movie)):
        if(letter==letters[i]):
            k+=1
    if(k!=0):
        return 1
    else:
        return 0

def unlock(qn,movie,letter):
    anslist=list(movie)
    qnlist=list(qn)
    for i in range (len(qn)):
        if(anslist[i]==letter):
            qnlist[i]=letter
    qn1="".join(str(x) for  x  in qnlist)
    return(qn1)

def check_ans(answer,movie):
    if(answer==movie):
        return 1
    else:
        return 0
    
def thanks(name1,name2,point1,point2):
    print(name1,". Your final score:",point1)
    print(name2,". Your final score:",point2)
    print("Thanks for Playing")
    print("Have a nice day")
    
def play():
    print("Welcome to Guess Game")
    print("Guess the names of the Legendary football players of all time...")
    p1=input("Player 1, Please enter your name.")
    p2=input("Player 2, Please enter your name.")
    pt1=0
    pt2=0
    turn=0
    while(1):
        if(turn%2==0):
            print(p1,", your turn.")
            pt=4
            n=0
            turn+=1
            said=True
            correct=choose()
            question=create_qn(correct)
            print("Question : ",question)
            while(said):
                k=int(input("Type 1 to give the answer or 0 to guess a letter. "))
                if(k==1 or n==3):
                    answer=input("Give the answer: ")
                    check=check_ans(answer,correct)
                    if(check==1):
                        print("Right Answer")
                        pt1=pt1+pt
                    else:
                        print("Sorry, Wrong Answer")
                    said=False
                else:
                    pt-=1
                    letter=input("Guess the letter: ")
                    s=is_present(letter,correct)
                    if(s==1):
                        unlocked=unlock(question,correct,letter)
                        question=unlocked
                        print("Letter present. Unlocked name: ",unlocked)
                    else:
                        print("Guessed letter,",letter,"not present.") 
                n+=1
            c=int(input("Enter 1 to continue or 0 to stop the game."))
            if(c==0):
                thanks(p1,p2,pt1,pt2)
                break
 
        else:
            print(p2,", your turn.")
            pt=4
            turn+=1
            n=0
            said=True
            correct=choose()
            question=create_qn(correct)
            print("Question : ",question)
            while(said):
                k=int(input("Type 1 to give the answer or 0 to guess a letter. "))
                if(k==1 or n==3):
                    answer=input("Give the answer: ")
                    check=check_ans(answer,correct)
                    if(check==1):
                        print("Right Answer")
                        pt2=pt2+pt
                    else:
                        print("Wrong Answer")
                    said=False
                else:
                    pt-=1
                    letter=input("Guess the letter: ")
                    s=is_present(letter,correct)
                    if(s==1):
                        unlocked=unlock(question,correct,letter)
                        question=unlocked
                        print("Letter present. Unlocked name: ",unlocked)
                    else:
                        print("Guessed letter,",letter,"not present.") 
                n+=1
            c=int(input("Enter 1 to continue or 0 to stop the game."))
            if(c==0):
                thanks(p1,p2,pt1,pt2)
                break