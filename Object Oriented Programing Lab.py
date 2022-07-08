# Module 9 Lab Object Oriented Programing

# Pet Class
class Pet():
    # Constructor
    def __init__(self, n, t, a):
        self.__name = n
        self.__type = t
        self.__age = a

    # Mutators
    def setName(self, n):
        self.__name = n

    def setType(self, t):
        self.__type = t

    def setAge(self, a):
        self.__age = a

    # Accessors
    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age

# main module
def main():
    #Initialize variable
    endProgram = 'no'
    #This while loop to run the program again
    while endProgram == 'no':
        # Get values for a pet
        inputName = input("Enter a pet's name:\n")
        inputType = input("Enter a pet's type:\n")
        inputAge = inputUser("Enter a pet's age:\n")

        # Create an object from the Pet class
        animal = Pet(inputName, inputType, inputAge)

        # Show values for this pet
        print('The pet name is', animal.getName())
        print('The pet type is', animal.getType())
        print('The pet age is', animal.getAge())

        #Ask the user
        endProgram = input('Do you want to end the program? (Enter yes or no)\n')
        #This while loop will checking the answer from users
        while endProgram != 'yes' and endProgram != 'no':
            print('Please enter yes or no')
            endProgram = input('Do you want to end the program?\n')
        if endProgram != 'yes':
            print()
            print('===== Please keep going! =====')
            print()
        elif endProgram != 'no':
            print()
            print('===== Thank you for using the program! =====')
            print()

#Input validation functions
def inputUser(msg):
    while True:
        try:
            num = int(input(msg))
            if not num < 0:
                return num
            print('No negative numbers')
        except:
            print('Please enter a whole numbers! No leters, negative numbers, or decimals')

main() # call main
