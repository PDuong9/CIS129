# CIS129 Programming and Problem Solving I
# 20781 SPRING 2022
# Module 6 EC Lab - Yum Yum Burger Joint
# Phong Duong

# The main function
def main():
    # Declare variables
    end_program = 'no'
    total_burger = 0
    total_fry = 0
    total_soda = 0
    burger_count = 0
    fry_count = 0
    soda_count = 0
    total = 0
    tax = 0
    sub_total = 0
    
    # Loop to run program again
    while end_program == 'no':
        # Reset variables
        total_burger = 0
        total_fry = 0
        total_soda = 0
        total = 0
        tax = 0
        sub_total = 0
        end_order = 'no'

        # Loop to take in order
        while end_order == 'no':
            print('Enter 1 for Yum Yum Burger')
            print('Enter 2 for Grease Yum Fries')
            print('Enter 3 for Soda Yum')
            option = input('Enter now -> ')
            if option == '1':
                # Call getBurger function
                total_burger = get_burger(burger_count, total_burger)
            elif option == '2':
                # Call getFry function
                total_fry = get_fry(fry_count, total_fry)
            elif option == '3':
                # Call getSoda function
                total_soda = get_soda(soda_count, total_soda)

            end_order = input('Do you want to end your order? (yes/no): ')

        # Call calcTotal function
        total = calc_total(total_burger, total_fry, total_soda, total, sub_total, tax)
        # Call printReceipt module
        printReceipt(total)
        end_program = input('Do you want to end program? (yes/no): ')

# getBurger function     
def get_burger(burger_count, total_burger):
    burger_count = float(input('Enter the number of burgers you want '))
    total_burger = total_burger + burger_count * .99
    return total_burger

# getFry function
def get_fry(fry_count, total_fry):
    fry_count = float(input('Enter the number of fries you want '))
    total_fry = total_fry + fry_count * .79
    return total_fry

# getSoda function 
def get_soda(soda_count, total_soda):
    soda_count = float(input('Enter the number of sodas you want '))
    total_soda = total_soda + soda_count * 1.09
    return total_soda

# calcTotal function
def calc_total(total_burger, total_fry, total_soda, total, sub_total, tax):
    sub_total = total_burger + total_fry + total_soda
    tax = sub_total * .06
    total = sub_total + tax
    total = round(total, 4)
    return total

# printReceipt module
def printReceipt(total):
    print('Your total is $', total)

# Call main function
main()