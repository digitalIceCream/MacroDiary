#!/usr/bin/python3
"""
Author:			John-Philipp Vogt
Date:			2022-09-08
Synopsis:		
Filename:		macroDiaryClasses.py
"""

# Classes

class meal:
    def __init__(self, name):
        self.name = name
        self.ingredients = {}
        self.totalMacros = {}
        
    def add_ingredient(self, ingredients):
        self.ingredients.update(ingredients)

    def sum_macros(self, macros):
        self.totalMacros.update(macros)

#########################################################
