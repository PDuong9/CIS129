# Lab 6 The Bottle Return Program
# Phong Duong
# March 30, 2022
# The program will keep track of the total number of bottles collected for 7 days. It will calculate the total number of bottles
# returned for the week and the amount paid out.

# The main function
def main():
    # Call welcomeMessage module
    displayWelcomeMessage('===== Welcome to The Bottle Return Program! =====')
    # Declare Integer totalBottles = 0
    total_bottles = 0
    # Declare Interger counter = 1
    counter = 1
    # Declare Integer todayBottles = 0
    today_bottles = 0
    # Declare Integer totalPayout = 0
    total_payout = 0
    # Declare String keepGoing = "y"
    keep_going = 'y'
    # While loop to run program again
    while keep_going == 'y':
        # Call getBottles function
        total_bottles = get_bottles()
        # Call calcPayout function
        total_payout = calc_payout(total_bottles)
        # Call printInfo module
        printInfo(total_bottles, total_payout)
        keep_going = input("Do you want to enter another week's worth of data?\n(Enter y or n)\n")
        if keep_going.lower() == 'n':
            print('===== Thank you for using program! =====')
            break

# WelcomeMessage module
def displayWelcomeMessage(message):
    print(message)

# getBottles function
def get_bottles():
    NBR_OF_DAYS = 7 
    # Declare and initialize totalBottles, todayBottles, counter to 0
    total_bottles = 0
    today_bottles = 0
    counter = 0
    while counter < 7:
        today_bottles = int(input('Enter number of bottles returned for day #' + str(counter + 1) + ': '))
        # Calculate the total number of bottles returned for the week
        total_bottles = total_bottles + today_bottles
        counter = counter + 1
    return total_bottles

# calcPayout function
def calc_payout(total_bottles):
    PAYOUT_PER_BOTTLE = .10
    # Reset to 0 for multuple runs
    total_payout = 0
    # Calculate the amount paid out
    total_payout = round(total_bottles * PAYOUT_PER_BOTTLE, 2)
    return total_payout

# printInfo module
def printInfo(total_bottles, total_payout):
    print('Your total number of bottle is ', total_bottles)
    print('Your payout is ', total_payout)

# call main function
main()