# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:59:58 2018

@author: conted
"""

import urllib.request
import os
from bs4 import BeautifulSoup

#a = os.open("D:\\Ali\\words.txt",'w')

response = urllib.request.urlopen("http://www.yahoo.com")
html = response.read().decode()
htm = BeautifulSoup(html,'html.parser')
#a = os.write(html)
#print( htm.decode())
lines2 = html.split("\n")
print(lines2, end ='\n')
#a.close()
#print(html)