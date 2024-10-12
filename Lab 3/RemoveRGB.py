''' Type your code here. '''

rValue = int(input())
gValue = int(input())
bValue = int(input())
minVal = rValue # initializes the minimum value as one of the input values

if gValue < rValue: # Checks if green is less than blue
    minVal = gValue
elif bValue < gValue: # Checks if blue is less than green
    minVal = bValue
elif rValue < bValue: # Checks if red is less than blue
    minVal = rValue

# minVal should now be the lowest of the three RGB values

rValue = rValue - minVal
gValue = gValue - minVal
bValue = bValue - minVal

print(rValue, gValue, bValue)