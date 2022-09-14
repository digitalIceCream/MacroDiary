#!/usr/bin/python3
"""
Author:			John-Philipp Vogt
Date:			2022-09-14
Synopsis:       Functions used in MacroDiary.py.
Filename:		MacroDiaryFunctions.py
"""
# Imports
import json


def get_choice() -> str:
    """ To guide the user through options """
    print('1 -- Show me today\'s total.')
    print('2 -- Record a new meal.')
    print('3 -- End programme.\n')
    choice = input('Your choice ->  ')
    return choice


def create_meal() -> tuple:
    """ Return object used throughout the functions as a container for all further user-input data """
    while True:
        meal_name = input('Give your meal a name ->  ')
        print('Is "', meal_name, '" correct? (y/n)')
        a = input().lower()
        if a == 'y':
            meal = {meal_name: None}
            return meal, meal_name
        else:
            print('Please try again.')
            continue


def add_ingredients(meal: dict, meal_name: str) -> tuple:
    """ Record ingredients and put them as one dict into top-level dict's value """
    index = 0
    ingredients = {}
    while True:
        print('Add up to 23 ingredients to', meal_name, 'and type "stop" when you are finished.')
        for a in range(23):
            print('Ingredient number', index + 1, 'in', meal_name, 'is...')
            b = input()
            if b != 'stop':
                ingredients.update({b: {'Fat': None, 'Carbs': None, 'Proteins': None}})
                index += 1
                continue
            elif b == 'stop':
                print('Your ingredients for', meal_name, 'are:')
                for c in ingredients.keys():
                    print(c)
                d = input('Is that correct? (y/n)  ').lower()
                if d == 'y':
                    meal.update({str(meal_name): ingredients})
                    return meal, meal_name
                else:
                    print('Start over then.')
                    ingredients.clear()
                    index = 0
                    continue
        break


def add_macros(meal: dict, meal_name: str) -> tuple:
    """ To add amount of fat, carbs, and proteins to each ingredient used in meal """
    while True:
        for key0, value0 in meal.items():
            print('For', key0, ':')
            for key1, value1 in value0.items():
                print('The ingredient', key1, 'contains this many grams of:')
                for key2, value2 in value1.items():
                    prompt = (key2 + ' -> ')
                    grams = input(prompt)
                    value1.update({key2: grams})

        #  In case of wrong input
        for key0, value0 in meal.items():
            for key1, value1 in value0.items():
                print(key1, 'contains:')
                for key2, value2 in value1.items():
                    print(value2, 'grams of', key2)
        a = input('Is this correct? (y/n)  ').lower()
        if a == 'y':
            return meal, meal_name
        else:
            print('Then start over')
            continue


def sum_macros(meal: dict, meal_name: str) -> tuple:
    """ To sum fats, carbs, and proteins of each ingredient to calculate meal's total macros """
    fat_in_total = 0
    carbs_in_total = 0
    proteins_in_total = 0
    while True:
        for key0, value0 in meal.items():
            for key1, value1 in value0.items():
                for key2, value2 in value1.items():
                    #  print(key2, value2)
                    if key2 == 'Fat':
                        fat_in_total += int(value2)
                    if key2 == 'Carbs':
                        carbs_in_total += int(value2)
                    if key2 == 'Proteins':
                        proteins_in_total += int(value2)

        #  total is kept separate: Could/should go into meal{}?
        total_macros = {str(meal_name): {'Fat': fat_in_total, 'Carbs': carbs_in_total, 'Proteins': proteins_in_total}}
        for key0, value0 in total_macros.items():
            for key1, value1 in value0.items():
                print(meal_name, 'contains in total', value1, 'grams of', key1)

        return meal, meal_name, total_macros


#  There's no practical use for this function, just for shits'n'giggles so far
def store_meal_as_json(today: str, meal: dict, meal_name: str, total_macros: dict):
    while True:
        a = input('Store meal? (y/n) ').lower()
        if a == 'y':
            filename = '_'.join([today, meal_name])
            filename = ''.join([filename, '.json'])
            with open(filename, 'a') as mealdotjson:
                json.dump(meal, mealdotjson)
            return

        else:
            print('Meal not stored.')
            break


def store_total_as_json(today: str, meal: dict, meal_name: str, total_macros: dict) -> None:
    """ To store total of a given meal for later data processing (daily totals)"""
    while True:
        a = input('Store total? (y/n) ').lower()
        if a == 'y':
            filename = '_'.join([today, meal_name, 'total'])
            filename = ''.join([filename, '.json'])
            with open(filename, 'a') as totaldotjson:
                json.dump(total_macros, totaldotjson)
            return

        else:
            print('Meal not stored.')
            break


def write_meal_to_file(today: str, meal: dict, meal_name: str, total_macros: dict) -> None:
    """ To keep a diary of meal as text"""
    while True:
        a = input('Write meal to diary? (y/n) ').lower()
        if a == 'y':
            filename = '_'.join([today, meal_name])
            with open(filename, 'a') as file:
                file.write('------------------------\n')
                file.write(today)
                file.write('\n')
                file.write(meal_name)
                file.write(' contains:\n')
                for key0, value0 in meal.items():
                    for key1, value1 in value0.items():
                        file.write(str(key1))
                        file.write('\n')
                        for key2, value2 in value1.items():
                            file.write(str(value2))
                            file.write(' grams of ')
                            file.write(str(key2))
                            file.write('\n')
                file.write('\n')
                file.write('In total:\n')
                for key0, value0 in total_macros.items():
                    for key1, value1 in value0.items():
                        file.write(str(value1))
                        file.write(' grams of ')
                        file.write(str(key1))
                        file.write('\n')
                file.write('\n------------------------\n\n')
                return
        else:
            print('Did not write to file.')
            break
