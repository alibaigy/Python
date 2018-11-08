# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:08:14 2018

@author: conted
"""

#def line(length):
#    shape=""
#    for i in range(length):
#        shape = shape + "*"
#    return shape
#
#
#def rectangle(x=3,y=3):
#    if x > 10 or x < 3:
#        x=3
#    if y > 10 or y < 3:
#        y=3
#    print(line(x))           
#    for j in range(y-2):
#        print("*",end="")
#        for i in range(x-2):
#            print(" ",end="")
#        print("*")    
#    print(line(x))       
#
#x=1
#while x !=0:
#    x=int(input("Enter width: "))
#    y=int(input("Enter height: "))
#    rectangle(x,y)






#name = ''
#student_marks = {}
#while name not in ('Q','q'):
#    name = input("Enter name: ")
#    if name in ('Q','q'):
#        break
#    mark = int(input("Enter mark : "))
#    student_marks[name] = mark
#for i,j in student_marks.items():
#    print(i,j)




#dic = {}
#string = input("Enter the string: ")
#for i in string:
#    i=i.lower()
#    dic[i] = dic.get(i,0) + 1
#    
#for i,j in sorted(dic.items()):
#     print(i,j)


fruits = {'Apples':10, 'Bananas':20, 'Oranges':15, 'Raisins':5, 'Apricots':8} 
print("1. Display inventory:")
print("2. Buy Fruits")         
print("3. Stock Fruits")         
print("4. Exit")
option = input("enter your selection: ")
while option != 4:
    if option == 1:
        for f,q in fruits.items():
            print(f,q)
    if option == 2:
        f = input("enter fruit name: ")
        while f not in fruits.keys():
            print("that fruit isn't in the list.")
            f = input("enter fruit name: ")
        q = int(input("How many you want? "))
        while q > fruits[f]:
               print("we don't have that many.")
               q = int(input("How many you want? "))
    option = input("enter your selection: ")
    
    