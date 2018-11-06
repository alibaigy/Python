# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:08:14 2018

@author: conted
"""

def line(length):
    shape=""
    for i in range(length):
        shape = shape + "*"
    return shape


def rectangle(x=3,y=3):
    if x > 10 or x < 3:
        x=3
    if y > 10 or y < 3:
        y=3
    print(line(x))           
    for j in range(y-2):
        print("*",end="")
        for i in range(x-2):
            print(" ",end="")
        print("*")    
    print(line(x))       


while x !=0:
    x=int(input("Enter width: "))
    y=int(input("Enter height: "))
    rectangle(x,y)