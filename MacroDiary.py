#!/usr/bin/python3
"""
Author:			John-Philipp Vogt
Date:			2022-09-08
Synopsis:		
Filename:		main.py
"""
# Imports

import datetime

# Functions

def create_meal():
    global mealName
    global meal
    while True:
        print("Give your meal a name.")
        mealName = input()

        print("Is \"",mealName,"\" correct? (y/n)")
        b = input().lower()

        if b == "y":
            meal = {mealName:None}
            break

        else:
            print("Please try again.")
            continue

def add_ingredients():
    global mealName
    global meal
    global ingredients
    ingredients = {}
    index = 0

    while True:
        print("Add up to 23 ingredients to",mealName ,"and type \"stop\" when you are finished.")
        for i in range(23):
            print("Ingredient number",index + 1,"is...")
            b = input()
            if b == "stop":
                print("Your ingredients are:")
                for i in ingredients.keys():
                    print(i)
                c = input("Is that correct? (y/n)  ")
                c = c.lower()
                if c == "y":
                    break
                else:
                    print("Start over then.")
                    ingredients.clear()
                    index = 0
                    continue
            else:
                ingredients.update({b: None})
                index += 1
                continue
        break

def add_macros():
    fat = "Fat"
    sumFat = 0.0
    global totalFat
    carbs = "Carbs"
    sumCarbs = 0.0
    global totalCarbs
    proteins = "Proteins"
    sumProteins = 0.0
    global totalProteins
    global ingredients
    global mealTotal
    global rollingTotal

    while True:
        check = True
        print("Add macros for \"", mealName,"\":")
        for x in ingredients:
            print(x,"has:")
            f = float(input("         Fat: "))
            c = float(input("         Carbs: "))
            p = float(input("         Proteins: "))
            a = input("Are those entries correct? (y/n) ")
            a = a.lower()
            if a == "y":
                sumFat += f
                sumCarbs += c
                sumProteins += p
                y = {fat: f, carbs: c, proteins: p}
                ingredients.update({x: y})
            else:
                print("Then start over.")
                ingredients.clear()
                check = False
                break
        if not check:
            continue
        mealTotal = {fat: sumFat, carbs: sumCarbs, proteins: sumProteins}
        totalFat += sumFat
        totalCarbs += sumCarbs
        totalProteins += sumProteins
        rollingTotal = {fat: totalFat, carbs: totalCarbs, proteins: totalProteins}
        break

# Main Program

totalFat = 0.0
totalCarbs = 0.0
totalProteins = 0.0

while True:
    create_meal()
    print(mealName, "created.")
    add_ingredients()
    add_macros()

    print(mealName,"has a total macro count of:")
    for k, v in mealTotal.items():
        print(k, v)

    print(datetime.date.today(),"has a rolling total of:")
    for k, v in rollingTotal.items():
        print(k, v)

    a = input("Add meal to diary? (y/n) ")
    a = a.lower()
    if a == "y":
        today = datetime.date.today()
        file = open(str(today), 'a')
        file.write(mealName)
        file.write(" has a total macro count of:\n")
        for k, v in mealTotal.items():
            macro = (k, v)
            file.write(str(macro))
            file.write("\n")
        file.write(str(today))
        file.write(" has a rolling total of:\n")
        for k, v in rollingTotal.items():
            total = (k, v)
            file.write(str(total))
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
