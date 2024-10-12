# A very similar problem to Threshold
# This time I use for-loops to show a difference in implementation
listLength = int(input())

# As usual, initialize an empty list
nums = []

for i in range(listLength):
    # Make sure that your inputs are floats
    # The compiler might fuss about if you try inputing a float as an int
    nums.append(float(input()))

# This loop is to find the largest num in the list
# Start off by making largestNum a very small number
# Iterate through the list and compare each element to 
#   your current value of largestNum
# DON'T NORMALIZE YET
largestNum = 0
for i in range(len(nums)):
    if nums[i] > largestNum:
        largestNum = nums[i]

# This loop is where the normalizing happens
# Inside the string literal, the brackets will
#   normalize the current element by the largest num
#   to 2 decimal places
for i in range(len(nums)):
    print(f'{(nums[i] / largestNum):.2f}')

