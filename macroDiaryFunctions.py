#!/usr/bin/python3
"""
Author:			John-Philipp Vogt
Date:			2022-09-08
Synopsis:		
Filename:		macroDiaryFunctions.py
"""
# Imports

# Functions

def create_meal():
    global mealName
    global meal
    while True:
        print("Give your meal a name.")
        mealName = input()

        print("Is \"",mealName,"\" correct? (y/n)")
        b = input()
        b = b.lower()

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
    carbs = "Carbs"
    sumCarbs = 0.0
    proteins = "Proteins"
    sumProteins = 0.0
    global ingredients
    global mealTotal

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
                sumFat = sumFat + f
                sumCarbs = sumCarbs + c
                sumProteins = sumProteins + p
                y = {fat: f, carbs: c, proteins: p}
                ingredients.update({x: y})
            else:
                print("Then start over.")
                check = False
                break
        if check == False:
            continue
        mealTotal = {fat: sumFat, carbs: sumCarbs, proteins: sumProteins}
        break
    return (sumFat, sumCarbs, sumProteins)

def rolling_total(a, b, c):
    global rolling_total
    totalFat
    rolling_total = {
            
