#!/usr/bin/python3
"""
Author:			John-Philipp Vogt
Date:			2022-09-08
Synopsis:		
Filename:		main.py
"""
# Imports

import datetime
import macroDiaryClasses as mdc
import macroDiaryFunctions as mdf

# Main Program

today = datetime.date.today()
print(today)
mdf.create_meal()
print(mdf.m1.name, "created.")
mdf.add_ingredients()
mdf.add_macros()
print(mdf.m1.name,"has a total macro count of:")
for k, v in mdf.m1.totalMacros.items():
    print(k, v)

a = input("Add meal to diary? (y/n) ")
a = a.lower()
if a == "y":
    file = open(str(today), 'a')
    file.write(mdf.m1.name)
    file.write(" has a total macro count of:\n")
    for k, v in mdf.m1.totalMacros.items():
        macro = (k, v)
        file.write(str(macro))
        file.write("\n")
    file.write("-------------------------------------")
    file.close()
else:
    print("Did not write to diary.")
####END PROMPT##########
print("End of program.")
