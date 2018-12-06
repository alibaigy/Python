# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:26:19 2018

@author: conted
"""
import json

country_list = []
for i in range(5):
    country = input("country: ")
    population = int(input("population: "))
    country_dict = {}
    country_dict = {country:population}
    country_list.append(country_dict)

a = open("test.json","w")
json.dump(country_list,a,indent= 4)
a.close  
    