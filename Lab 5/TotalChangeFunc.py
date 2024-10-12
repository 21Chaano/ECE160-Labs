# Introducing the ExactChange from lab 3, now as a function!

# This function is very similar to how we found the number
#   of coins in ExactChange.py from lab 3
# Refer to ExactChange.py for explanation of the math
def exact_change(user_total):
    numQuarters = user_total // 25
    user_total  = user_total  % 25

    numDimes    = user_total // 10
    user_total  = user_total  % 10

    numNickels  = user_total //  5
    numPennies  = user_total  %  5

    # This time, we want to return a tuple
    # Simply wrap the variables in parentheses
    return (numPennies, numNickels, numDimes, numQuarters)

if __name__ == '__main__': 
    input_val = int(input())    
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)

    # Instead of printing in the function, 
    #   we print out here in main

    # This checks the case where no change is needed
    if input_val == 0:
        print('no change')

    # The following branches checks for singular/plural/none
    # IMPORTANT: Pay attention to the example outputs the 
    #   problems give you. If you just copy paste from Lab 3,
    #   you will fail the compare output tests
    if num_pennies >  1:
        print(f'{num_pennies} pennies')
    elif num_pennies == 1:
        print(f'{num_pennies} penny')

    if num_nickels >  1:
        print(f'{num_nickels} nickels')
    elif num_nickels == 1:
        print(f'{num_nickels} nickel')

    if num_dimes >  1:
        print(f'{num_dimes} dimes')
    elif num_dimes == 1:
        print(f'{num_dimes} dime')

    if num_quarters >  1:
        print(f'{num_quarters} quarters')
    elif num_quarters == 1:
        print(f'{num_quarters} quarter')
    
    