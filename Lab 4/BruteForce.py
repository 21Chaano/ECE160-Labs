''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

# You don't need to use a boolean for this problem
# Booleans can be useful to validate cases where you need to validate something
foundSoln = False

# Be careful when making these kinds of nested loops
# One wrong line of code and you might end up printing something way too many times
# In solving this, I ran into a bug where I printed "There is no solution" 21^21 times
for x in range(-10, 11):
    for y in range(-10, 11): # Remember that range will exclude the last number in the range
        # This if-statement only executes once we find an x and y value that satisfies both equations
        # If all goes to plan, this branch will only be entered once and the code will continue on
        if ((a*x) + (b*y)) == c and ((d*x) + (e*y)) == f:
            print(f'x = {x} , y = {y}')
            foundSoln = True
            break # This line might be unnecessary, as it only breaks out of the inner loop. The outer loop will still continue

# The not keyword will check for the opposite of whatever you are checking
# Think of it like "==" vs "!="
# In this case, if we did not find a solution, then the if-statement is true
if not foundSoln:
    print("There is no solution")