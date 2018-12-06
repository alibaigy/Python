# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:39:22 2018

@author: conted
"""

#
#
#myDeck = pc.SCardDeck()
#myhand01 = pc.SHand("John")
#
#myhand01.hit(myDeck)
#myhand01_value = myhand01.get_value()
#
#print(myhand01_value)
#print( format(myhand01.owner,myhand01,myhand01_value))

import pythoncards as pc

player1 = input("Enter player 1: ")
player2 = input("Enter player 2: ")
myDeck = pc.SCardDeck()

repeat = "y"

try:
    while repeat == "y":
        hand1 = pc.SHand(player1)
        hand2 = pc.SHand(player2)
        for i in range (5):
            hand1.hit(myDeck)
            hand2.hit(myDeck)
        v1 = hand1.get_value()
        v2 = hand2.get_value()
        print('%10s  %10s  %5s'%(player1,hand1,v1))
        print('%10s  %10s  %5s'%(player2,hand2,v2))
        if v1 > v2:
            print(player1," is the winner: ",v1)
        elif v1 < v2:
            print(player2," is the winner: ",v2)
        else:
            print("congrats, that's a tie!")
        repeat = input("do you want to play again? (y/n) : ")
        if repeat not in ("y","n"):
            repeat = "n"
except:
    print("Sorry, not enough cards left !!")

