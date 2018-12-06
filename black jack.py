# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:53:47 2018

@author: conted
"""

import pythoncards as pc

player = input("So what's your name? ")
myDeck = pc.SCardDeck()

repeat = 'y'
while repeat == 'y':
    Hand = pc.SHand(player)
    Dealer = pc.SHand("Dealer")
    
    for i in range (2):
        Hand.hit(myDeck)
        Dealer.hit(myDeck)
    print(Hand.cards)
    winner = ''    
    vh = Hand.get_value()
    vd = Dealer.get_value()
    print('%10s  %10s  %5s'%(player,Hand,vh))
    print('%10s  %10s  %5s'%("Dealer",Dealer,vd))
    if vh > vd:
        winner ='h'
    elif vh < vd:
        winner = 'd'
    else:
        winner = 't'
    while vh < 22 and vd < 22:
        choice= input("Would you like to hit or stand? (h/s) ")
        if choice == 'h':
            Hand.hit(myDeck)
        else:
            Dealer.hit(myDeck)
        vh = Hand.get_value()
        vd = Dealer.get_value()
        print('%10s  %10s  %5s'%(player,Hand,vh))
        print('%10s  %10s  %5s'%("Dealer",Dealer,vd))
    
        if vh > vd and vh < 22 :
            winner ='h'
        elif vh < vd and vd < 22:
            winner = 'd'
        else:
            winner = 't'
    if winner == 'h':
        print("Dealer is busted, you won !")
    elif winner == 'd':
        print("You're busted, Dealer won !" )
    else:
        print("WOW, that was a tie !")
    repeat = input("you wanna play again? (y/n) ")
