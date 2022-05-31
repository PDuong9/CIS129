'''
Module 4 Lab Hot Dog Cookout Calculator
'''

# Import math.ceil library
import math
# Main module
def main():
# Input
    total = getTotalHotDogs()
    DOGS = 10
    BUNS = 8

    # Calculate the number of left over hot dogs. (% = MOD)
    dogsLeft = (DOGS - total % DOGS) % DOGS
    # Calculate the minimum number of packages of hot dogs.
    minDogs = math.ceil(total / DOGS)
    # Calculate the number of left over hot dog buns.
    bunsLeft = (BUNS - total % BUNS) % BUNS
    # Calculate the minimum number of packages of hot dogs buns.
    minBuns = math.ceil(total / BUNS)
    
    showResults(dogsLeft, minDogs, bunsLeft, minBuns)
# End main module

# Function getTotalHotDogs()
def getTotalHotDogs():
    print('Enter the number of people attending the cookout: ')
    people = int(input())
    print('Enter the number of hot dogs for each person: ')
    hotDogs = int(input())
    total = people * hotDogs
    return total
# End getTotalHotDogs()

# Module showResults() 
def showResults(dogsLeft, minDogs, bunsLeft, minBuns):
    print('Minimum packages of hot dogs needed: ', minDogs)
    print('Minimum packages of hot dogs buns needed: ', minBuns)
    print('Hot dogs left over: ', dogsLeft)
    print('Hot dog buns left over: ', bunsLeft)
# End showResults()

main()
# Calls the main module