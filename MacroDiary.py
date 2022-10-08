#!/usr/bin/python3
"""
Author:			John-Philipp Vogt
Date:			2022-09-14
Synopsis:		A CLI programme that guides the user to record a single meal with its weighted macros.
                It writes the user input to file, showing the name of the meal, its ingredients and their macro
                nutrients content, as provided by the user. It also stores the input encoded in json separately.
                Technically, all user input it inserted into dicts{}, resulting in nested dicts{}.
Filename:		MacroDiary.py
"""
# Imports
import MacroDiaryFunctions as mdf
import ChoiceOne as c1
import ChoiceTwo as c2
import ChoiceThree as c3
import datetime
# import json
# import pprint

# Main program -- prep
today = str(datetime.date.today())

# Main program -- exec

print('Welcome to the MacroDiary!!\nWhat do you want to do?')

# Main programme loop
while True:
    choice = mdf.get_choice()
    if choice == '1':  # Shows today's total (tbi)
        print('Placeholder')
        #  Insert function here that retrieves all totals for a given day (or just today).
        #  It should retrieve those that mdf.store_total_as_json() can write to storage.
        #  It should then sum them up and display the sum.
        #  And then it should continue to the main menu.
        continue

    elif choice == '2':  # Record a new meal
        meal = mdf.create_meal()  # Creates data structure ({'name': None}), and a name (str), returns as tuple
        meal = mdf.add_ingredients(meal[0], meal[1])  # Adds ingredients as dicts to previous dict, returns tuple
        meal = mdf.add_macros(meal[0], meal[1])  # Adds macros as dicts to previous dict, returns tuple
        meal = mdf.sum_macros(meal[0], meal[1])  # Sums given macros for meal, returns tuple
        mdf.store_meal_as_json(today, meal[0], meal[1], meal[2])  # Writes json-encoded dict to file
        mdf.store_total_as_json(today, meal[0], meal[1], meal[2])  # Write json-encoded dict to file
        mdf.write_meal_to_file(today, meal[0], meal[1], meal[2])  # Writes meal, ingredients, macros and total to file
        continue

    elif choice == '3':  # Exits
        print('Exiting programme.')
        break

    else:  # Input confirmation
        print('Invalid input')
        continue

print("End of program.")  # Signal prompt that the show is over
