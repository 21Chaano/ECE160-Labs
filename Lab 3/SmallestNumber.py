''' Type your code here. '''

num1 = int(input())
num2 = int(input())
num3 = int(input())

smallest = num1 # Initialize smallest as any of the values

# I compare the three numbers in a triangular way
# Check each number to the number "next" to it as if they were points on a triangle
if num2 < num1:
    smallest = num2
if num3 < num2:
    smallest = num3
if num1 < num3:
    smallest = num1

# After comparing the numbers to their neighbors, smallest is guaranteed to be the smallest of the three
print(smallest)