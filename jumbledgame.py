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

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thanks(name1,name2,point1,point2):
    print(name1,". Your final score:",point1)
    print(name2,". Your final score:",point2)
    print("Thanks for Playing")
    print("Have a nice day")
    
def play():
    print("Welcome to Guess Game")
    print("Rearrange the letters to get names of the Legendary football players of all time...")
    p1=input("Player 1, Please enter your name.")
    p2=input("Player 2, Please enter your name.")
    pt1=0
    pt2=0
    turn=0
    while(1):
        if(turn%2==0):
            print(p1,", your turn.")
            turn+=1
            correct=choose()
            jumbledword=jumble(correct)
            print("What is on your mind? :",jumbledword)
            guess=input("Answer:")
            if(guess==correct):
                pt1+=1
                print("Right Answer.",correct)
            else:
                print("Wrong Answer. Better luck next time. Correct answer is:",correct)
            print(p1,"Your score is:",pt1)
            c=int(input("Enter 1 to continue or 0 to stop the game."))
            if(c==0):
                thanks(p1,p2,pt1,pt2)
                break
        else:
            print(p2,", your turn.")
            turn+=1
            correct=choose()
            jumbledword=jumble(correct)
            print()
            print("What is on your mind?:",jumbledword)
            guess=input("Answer:")
            if(guess==correct):
                pt2+=1
                print("Right Answer.",correct)
            else:
                print("Wrong Answer. Better luck next time. Correct answer is:",correct)
            print(p2,"Your score is:",pt2)
            c=int(input("Enter 1 to continue or 0 to stop the game."))
            if(c==0):
                thanks(p1,p2,pt1,pt2)
                break
    