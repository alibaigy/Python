# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:31:48 2018

@author: conted
"""

import os

os.chdir("..\\..\\")
print(os.getcwd())
os.chdir(".\\Ali")
print(os.getcwd())
#os.mkdir("test")
print(os.listdir())
print(os.listdir()[2])