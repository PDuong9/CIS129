# Module 9 Lab Object Oriented Programing
# CIS 129 Programing and Problem Solving I
# Phong Duong

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

    # Get values for a pet
    inputName = input("Enter a pet's name:\n")
    inputType = input("Enter a pet's type:\n")
    inputAge = int(input("Enter a pet's age:\n"))

    # Create an object from the Pet class
    animal = Pet(inputName, inputType, inputAge)

    # Show values for this pet
    print('The pet name is', animal.getName())
    print('The pet type is', animal.getType())
    print('The pet age is', animal.getAge())

main() # call main
