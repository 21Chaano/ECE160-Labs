# This module is more of a problem on how 
#   to take in an unknown number of inputs
# 
# This is an example of the case where using 
#   a while-loop is easier than using a for-loop

# There are multiple ways to implement the code
# I start this off by taking an initial input
# Then initializing an empty list
num = int(input())
nums = []

while num > 0:
    # Start with appending the old value of num
    # If you take an input before appending,
    # You might exclude/include unexpected values
    nums.append(num)
    num = int(input())

# The min() and max() methods will find the 
#   smallest and largest values for you
print(f'{min(nums)} and {max(nums)}')

###################################################
# Here is another solution:
#
# nums = []
# while True:
#    num = int(input())
#    if num > 0:
#        nums.append(num)
#    else:
#        break
#
# print(f'{min(nums)} and {max(nums)}')
#
###################################################