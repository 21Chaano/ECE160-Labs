# Functions are very useful things in programming languages
# They make writing code a lot more simple and easier to read
# Your function definitions will always be above your main
# Functions typically take in a parameter that will be defined
#   later in main. You can use the parameters, just don't define
#   them in the functions
def laps_to_miles(user_laps):
    # Here I define a variable then return the variable
    # In a simple function like this, you could simply
    #   return the equation itself
    milesRan = user_laps * 0.25
    return milesRan

# If you have functions, DO NOT forget to include this part
# if__name__ == '__main__': is what the unit tests will look for
# when testing your code.
# If you don't have this block, the unit test will likely fail
if __name__ == '__main__':
    numLaps = float(input())
    print(f'{laps_to_miles(numLaps):.2f}')