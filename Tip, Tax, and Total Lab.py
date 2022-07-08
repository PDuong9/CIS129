# CIS129 Programing and Problem Solving I
# Instructor: Brittany Griwzow
# Module 5 EC Lab - Tip, Tax, and Total
# Phong Duong

# Global Constant variable for the 6% tax on a meal price
TAX = 0.06
# Global Constant variable for the 10% tip in meal price range from .01 to 5.99
TIP_P_1 = 0.1
# Global Constant variable for the 10% tip in meal price range from 6 to 12.00
TIP_P_2 = 0.13
# Global Constant variable for the 10% tip in meal price range from 12.01 to 17.00
TIP_P_3 = 0.16
# Global Constant variable for the 10% tip in meal price range from 17.01 to 25.00
TIP_P_4 = 0.19
# Global Constant variable for the 10% tip in meal price range from 25.01 and more
TIP_P_5 = 0.22

# main module
def main():
    # Call the input function to get data from users
    mealPrice = input_price('Enter the meal price $')
    # Call the tax function
    tax = calc_tax(mealPrice)
    # Call the tip function
    tip = calc_tip(mealPrice + tax)
    # Call the total function
    total = calc_total(mealPrice, tip, tax)
    # Display the results
    print_values(mealPrice, total, tip, tax)

# The input_price function gets the meal price that users will be given.
def input_price(prompt):
    mealPrice = float(input(prompt))
    return mealPrice

# The calc_tip function will calculates the tip.
def calc_tip(mealPrice):
    if mealPrice >= 0.01 and mealPrice <= 5.99:
        tip = mealPrice * TIP_P_1
    elif mealPrice >= 6 and mealPrice <= 12.00:
        tip = mealPrice * TIP_P_2
    elif mealPrice >= 12.01 and mealPrice <= 17.00:
        tip = mealPrice * TIP_P_3
    elif mealPrice >= 17.01 and mealPrice <= 25.00:
        tip = mealPrice * TIP_P_4
    else: 
        tip = mealPrice * TIP_P_5
    # The result will be rounded to 2 decimal.
    tip = round(tip, 2)
    return tip

# The calc_tax function will calculates the tax.
def calc_tax(mealPrice):
    tax = mealPrice * TAX
    # The result will be rounded to 2 decimal.
    tax = round(tax, 2)
    return tax

# The calc_total function will calculates the total.
def calc_total(mealPrice, tip, tax):
    total = mealPrice + tip + tax
    # The total will be rounded to 2 decimal.
    total = round(total, 2)
    return total

# The print_values accepts the meal price as an argument and calculates the tip, the tax
# and the total, and displays the results.
def print_values(mealPrice, total, tip, tax):
    print('The meal price $', mealPrice)
    print('The tip is $', tip)
    print('The tax is $', tax)
    print('The total is $', total)

# call main
main()