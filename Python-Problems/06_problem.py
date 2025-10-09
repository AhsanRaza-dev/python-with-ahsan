'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

i.e.: ahsan raza -> Ahsan Raza
Given a full name, your task is to capitalize the name appropriately.
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # Initialize an empty string to store the final result
    result = ""
    
    # Loop through each character in the input string
    for i in range(len(s)):
        # Check if current character should be capitalized:
        #  If it's the first character of the string
        #  OR if the character before it is a space (' ')
        if i == 0 or s[i - 1] == ' ':
            result += s[i].upper()   # Convert it to uppercase
        else:
            result += s[i]           # Otherwise, keep it as is
    
    # Return the final capitalized string
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

