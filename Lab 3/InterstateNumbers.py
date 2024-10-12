highway_number = int(input())

# This is a bit more compared to the previous lab problems
# There are many ways to solve this, each with varying levels of "messiness"
# The solution below is the cleanest way I was able to come up with

# Code for set up
serviceHighway = highway_number % 100 # Take the last to digits of highway_number
# any number % 2 can either be 0 or 1. 
# 0 means there is no remainder and thus an even number
# 1 means it is odd because the number cannot be divided evenly by 2
# An aside: when you use modulo, the returned value will always be a max of the dividend - 1
# Ex. num % 63 can be anywhere in range(0, 63)
# It won't include 63 because that means you have enough parts to complete a whole
if (highway_number % 2) == 0:
    direction = 'east/west'
elif (highway_number % 2) == 1:
    direction = 'north/south'
    
# Code for execution
# In branching, the "and" and "or" keywords can be used to connect conditionals
# If you use "or", the computer will enter the branch if at least one of the conditionals are true
# If you use "and", the computer will enter the branch if both conditionals are true
if (serviceHighway == 0) or (highway_number == 0):
    print(f'{highway_number} is not a valid interstate highway number.')
else:
    if (highway_number // 100) != 0:
        print(f'I-{highway_number} is auxiliary, serving I-{serviceHighway}, going {direction}.')
    else:
        print(f'I-{highway_number} is primary, going {direction}.')