# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:57:28 2018

@author: conted
"""
#
import os
#dir = os.getcwd()
#print(dir)
#for name in os.listdir():
#    if len(name) <= 9:
#        print(name)
#name = input("input file name")
#if os.path.isfile(name):
#    print("exists")
#else:
#    print("doesn't exist")
#    
#    
#os.chdir("..\\Big_data_course")
#print(os.getcwd())

#os.chdir("..\\Python")
f= open("test.txt",'r')
for i in f:
    print(i,end='')
f.close
f=open("test.txt",'a')    
string = input("- ")
while string.lower() !='q':
    f.write("\n")
    f.write(string)
    string= input("- ")
f.flush
f.close()
#f= open("test.txt",'r')
#f.close