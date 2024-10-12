def feet_to_steps(user_feet):
    # Remember that floor division rounds
    #   down to the nearest integer
    numSteps = user_feet // 2.5
    return numSteps

if __name__ == '__main__':
    feetTraveled  = float(input())
    # You can assign a function call to a variable
    # Doing this rather than printing the return value
    #   can be much more clear when looking back at code
    stepsTraveled = feet_to_steps(feetTraveled)

    # The output expects 0 decimal places, but 
    #   feet_to_steps returns a float
    # We still need the .0f
    print(f'{stepsTraveled:.0f}')