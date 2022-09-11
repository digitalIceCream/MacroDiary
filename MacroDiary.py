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

global total

while True:
    mdf.create_meal()
    print(mdf.mealName, "created.")
    mdf.add_ingredients()
    print(mdf.ingredients)
    mdf.add_macros()
    """
    print(mdf.meal.name,"has a total macro count of:")
    for k, v in mdf.meal.totalMacros.items():
        print(k, v)

    print("Rolling Total so far for:")
    for k, v in total.items():
        print(k, v)

    a = input("Add meal to diary? (y/n) ")
    a = a.lower()
    if a == "y":
        today = datetime.date.today()
        file = open(str(today), 'a')
        file.write(mdf.meal.name)
        file.write(" has a total macro count of:\n")
        for k, v in mdf.meal.totalMacros.items():
            macro = (k, v)
            file.write(str(macro))
            file.write("\n")
        file.write("-------------------------------------")
        file.write("\n\n")
        file.close()
        continue
    """
    #else:
    print("Did not write to diary.")
    #    break

####END PROMPT##########

print("End of program.")
