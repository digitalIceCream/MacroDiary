#!/usr/bin/python3
"""
Author:			John-Philipp Vogt
Date:			2022-09-08
Synopsis:		
Filename:		main.py
"""
# Imports

import datetime
import macroDiaryFunctions as mdf

# Main Program

global meal
global mealName
global ingredients
global mealTotal
global total
global totalFat 
totalFat = 0.0
global totalCarbs
totalCarbs = 0.0
global totalProteins
totalProteins = 0.0
global rollingTotal 

while True:
    mdf.create_meal()
    print(mdf.mealName, "created.")
    mdf.add_ingredients()
    mdf.add_macros()

    print(mdf.mealName,"has a total macro count of:")
    for k, v in mdf.mealTotal.items():
        print(k, v)

    print(datetime.date.today(),"has a rolling total of:")
    for k, v in mdf.rollingTotal.items():
        print(k, v)

    a = input("Add meal to diary? (y/n) ")
    a = a.lower()
    if a == "y":
        today = datetime.date.today()
        file = open(str(today), 'a')
        file.write(mdf.mealName)
        file.write(" has a total macro count of:\n")
        for k, v in mdf.mealTotal.items():
            macro = (k, v)
            file.write(str(macro))
            file.write("\n")
        file.write("-------------------------------------")
        file.write("\n\n")
        file.close()
        continue
    else:
        print("Did not write to diary.")
        break
####END PROMPT##########

print("End of program.")
