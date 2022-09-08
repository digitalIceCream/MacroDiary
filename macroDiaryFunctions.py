#!/usr/bin/python3
"""
Author:			John-Philipp Vogt
Date:			2022-09-08
Synopsis:		
Filename:		macroDiaryFunctions.py
"""
# Imports

import macroDiaryClasses as mdc

# Functions

def create_meal():
    while True:
        print("Give your meal a name.")
        a = input()

        print("Is \"",a,"\" correct? (y/n)")
        b = input()
        b = b.lower()

        if b == "y":
            global m1
            m1 = mdc.meal(a)
            break

        else:
            print("Please try again.")
            continue

def add_ingredients():
    index = 0
    global ingredients
    ingredients = []

    while True:
        print("Add up to 23 ingredients to",m1.name,"and type \"stop\" when you are finished.")
        for i in range(23):
            print("Ingredient number",index + 1,"is...")
            a = input()
            if a == "stop":
                print("Your ingredients are:")
                for i in ingredients:
                    print(i)
                b = input("Is that correct? (y/n)  ")
                b = b.lower()
                if b == "y":
                    break
                else:
                    print("Start over then.")
                    ingredients.clear()
                    index = 0
                    continue
            else:
                ingredients.append(a)
                index += 1
                continue
        break
    
def add_macros():
    fat = "Fat"
    sumFat = 0
    carbs = "Carbs"
    sumCarbs = 0
    proteins = "Proteins"
    sumProteins = 0

    while True:
        check = True
        print("Add macros for \"", m1.name,"\":")
        for x in ingredients:
            print(x,"has:")
            f = input("         Fat: ")
            c = input("         Carbs: ")
            p = input("         Proteins: ")
            a = input("Are those entries correct? (y/n) ")
            a = a.lower()
            if a == "y":
                sumFat = sumFat + float(f)
                sumCarbs = sumCarbs + float(c)
                sumProteins = sumProteins + float(p)
                y = {fat: f, carbs: c, proteins: p}
                m1.add_ingredient({x: y})
            else:
                print("Then start over.")
                check = False
                break
        if check == False:
            continue
        m1.sum_macros({fat: sumFat, carbs: sumCarbs, proteins: sumProteins})
        break
