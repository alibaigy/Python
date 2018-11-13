# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:31:48 2018

@author: conted
"""

import os

#os.chdir("..\\..\\")
#print(os.getcwd())
#os.chdir(".\\Ali")
#print(os.getcwd())
##os.mkdir("test")
#print(os.listdir())
#print(os.listdir()[2])
#if os.path.isdir("Python"):
#    print("There's a folder named Python in this directory")

os.chdir("d:\\Ali\\python")
#print(os.getcwd())
#filelist = os.listdir()
#for files in filelist:
#    if os.path.isfile(files):
#        print(files)

f= open("IDEs.txt",'r')
for line in f:
    print (line, end ='')
f.close

fcreate = open("test.txt","w")
fcreate.write("this is a test file.\n Now see the result.")
fcreate.close

#bringing back the pointer to start of the file:
f.seek(0)