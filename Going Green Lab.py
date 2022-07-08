# Module 8 Going Green Lab


#Constant variable for arrays
SIZE = 12
#define main
def main():
    #Initialize variable
    endProgram = 'no'
    #This while loop to run program again
    while endProgram == 'no':
        notGreenCost = [0] * SIZE
        goneGreenCost = [0] * SIZE
        savings = [0] * SIZE
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        #The program starts
        print()
        print('=== Welcome to the GREEN or NOT GREEN savings calculator program! ===')
        print()
        #This array will get not green costs input from users
        for i in range(len(months)):
            msg = 'Enter NOT GREEN energy costs for ' + months[i]+'\nEnter now --> $'
            notGreenCost[i] = userInput(msg)

        print('---------------------------------------------------------------------')
        #This array will get gone green costs input from users
        for i in range(len(months)):
            msg = 'Enter GONE GREEN energy costs for ' + months[i]+'\nEnter now --> $'
            goneGreenCost[i] = userInput(msg)
        #This array will calculate savings cost for users
        for i in range(len(months)):
            savings[i] = notGreenCost[i] - goneGreenCost[i]
        #Call outcome module 
        displayOutcome(savings, notGreenCost, goneGreenCost, months)
        #Ask the user
        endProgram = input('Do you want to end the program? (Enter yes or no)\n')
        #This while loop will checking the answer from users
        while endProgram != 'yes' and endProgram != 'no':
            print('Please enter yes or no')
            endProgram = input('Do you want to end the program?\n')
        #The program ends when main is over
        print()
        print('=== Thank you for using the program! ===')
        print()
#Input validation functions
def userInput(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except:
            print('Please enter a whole number! No leters or decimals')
#Outcome function
def displayOutcome(savings, notgreen, green, months):
    # Outcome table
    print('---------------------------------------------------------------------')
    print('\t\t\t\t' + 'SAVINGS')
    print('__________________________________________________________________________')
    print('SAVINGS' + '\t\t' + 'NOT GREEN' + '\t\t' + 'GONE GREEN' + '\t\t' + 'MONTHS')
    print('__________________________________________________________________________')
    #This array will display all data in table
    for i in range(SIZE):
        # \t is TAB the line
        print('$ '+str(savings[i]) + '\t\t' + '$ ' + str(notgreen[i]) + '\t\t\t' + '$ ' + str(green[i]) + '\t\t\t' + months[i] +'\n')

main() # call main