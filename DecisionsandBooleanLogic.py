# Module 5 Lab-5
# The program will help the company calculate the amount of bonuses that the store and each
# individual employee will receive based on the total monthly sales and the percentage
# increase in sales.

# The main function
def main():
    # call to get sales
    monthly_sales = get_sales('Enter the monthly sales $')
    # call to get sales increase
    sales_increase = get_increase('Enter percent of sales increase: ')
    # call to get the store bonus
    store_amount = calc_store_bonus(monthly_sales)
    # call to get the employee bonus
    emp_amount = calc_emp_bonus(sales_increase)
    # call to print amounts
    print_bonus(store_amount, emp_amount)

# This function gets the monthly sales
def get_sales(prompt):
    monthly_sales = float(input(prompt))
    return monthly_sales

# This function gets the percent of increase in sales
def get_increase(prompt):
    sales_increase = float(input(prompt))
    sales_increase = sales_increase / 100
    return sales_increase


# This function determines the storeAmount bonus
def calc_store_bonus(monthly_sales):
    if monthly_sales >= 110000:
        store_amount = 6000
    elif monthly_sales >= 100000:
        store_amount = 5000
    elif monthly_sales >= 90000:
        store_amount = 4000
    elif monthly_sales >= 80000:
        store_amount = 3000
    else:
        store_amount = 0
    return store_amount

# This function determines the emp_amount bonus
def calc_emp_bonus(sales_increase):
    if sales_increase >= 0.05:
        emp_amount = 75
    elif sales_increase >= 0.04:
        emp_amount = 50
    elif sales_increase >= 0.03:
        emp_amount = 40
    else:
        emp_amount = 0
    return emp_amount

# This function print the bonus information
def print_bonus(store_amount, emp_amount):
    print('The store bonus amount is $', store_amount)
    print('The employee bonus amount is $', emp_amount)
    if store_amount == 6000 and emp_amount == 75:
        print('Congrats! You have reached the highest bonus amounts possible!')

# call main
main()