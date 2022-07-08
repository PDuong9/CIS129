# Lab 7 Theater Seating Lab
# CIS 129 Programming and Problem Solving I
# Phong Duong

# Constant variables each seating section
SEAT_SECTION_A = 300
SEAT_SECTION_B = 500
SEAT_SECTION_C = 200
# Constant variables each seats cost 
SECTION_A_COST = 20
SECTION_B_COST = 15
SECTION_C_COST = 10
# main function 
def main():
    print()
    # call to show message display
    showMessageDisplay('Welcome to the Theater Sating program!')
    # initialize variables
    end_program = 'no'
    # while loop to run program again
    while end_program == 'no':
        # call to getValidTickets 
        seat_a = get_valid_tickets('Please enter number of ticket sold in section A:\n', 0, SEAT_SECTION_A)
        seat_b = get_valid_tickets('Please enter number of ticket sold in section B:\n', 0, SEAT_SECTION_B)
        seat_c = get_valid_tickets('Please enter number of ticket sold in section C:\n', 0, SEAT_SECTION_C)
        # call to getTotal       
        total_a = get_total(SECTION_A_COST, seat_a)
        total_b = get_total(SECTION_B_COST, seat_b)
        total_c = get_total(SECTION_C_COST, seat_c)
        # calculation for overall total
        total = total_a + total_b + total_c
        # call to display outcome 
        displayOutcome('A', total_a, seat_a)
        displayOutcome('B', total_b, seat_b)
        displayOutcome('C', total_c, seat_c)
        # display the overall total
        print('The overall total $',total)
        end_program = input('Do you want to end the program? (yes or no)\n')
    print('Thank you for using this program!')
# this function displays message
def showMessageDisplay(hello):
    print(hello)
# this function gets user input
def get_ticket(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print('Please enter a whole number! No letter or decimals!')
# this function will process the data that users input
def get_valid_tickets(msg, low, high):
    user_input = get_ticket(msg)
    while user_input < low or user_input > high:
        user_input = get_ticket(msg)
    return user_input
# this function calculates each section
def get_total(cost, seat):
    total = cost * seat
    return total
# this function displays total
def displayOutcome(section, total, ticket):
    print('The total of section '+ section +' $' + str(total) + ' number tickets ' + str(ticket))
# calls main
main()