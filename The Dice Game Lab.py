# Lab 7-3 The Dice Game
# CIS 129 Programming and Problem Solving I
# Phong Duong

# import library
import random
# the main function
def main():
    print()
    # initialize variables
    end_program = 'no'
    player_one = 'NO NAME'
    player_two = 'NO NAME'
    # while loop to run program again
    while end_program == 'no':
        # populate variable
        winners_name = 'NO NAME'
        p1number = 0
        p2number = 0
        # call to inputNames
        player_one, player_two = input_names(player_one, player_two)
        # call to rollDice
        winners_name = roll_dice(p1number, p2number, player_one, player_two, winners_name)
        # call to displayInfo
        displayInfo(winners_name)
        end_program = input('Do you want to end program? (yes/no): ')

# this function gets the players names
def input_names(player_one, player_two):
    player_one = input('Please enter the name of player one: ')
    player_two = input('Please enter the name of player two: ')
    return player_one, player_two

# this function will get the random values
def roll_dice(p1number, p2number, player_one, player_two, winners_name):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    if p1number > p2number:
        winners_name = player_one
    elif p2number > p1number:
        winners_name = player_two
    else:
        winners_name = 'TIE'
    return winners_name

# this function displays the winner 
def displayInfo(winners_name):
    print('You are the winner!', winners_name)

# calls main
main()