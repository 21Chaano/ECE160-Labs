userNum = int(input())

# I use an if-else on the outside of the loop to check if userNum is in the valid range.
# We don't want to do anything with userNum if it's not between 11 and 99 inclusive
if (userNum < 11) or (userNum > 99):
    print('Input must be 11-99')
else:
    # The idea for this conditional is from a student in this class
    # I never thought to do this but I found it impressive and clever, so I'll use it here
    # The conditional used in the while-loop makes use of // and % to get the ten's place and one's place respectively
    # If they are not equal, then print userNum and decrement by 1
    while (userNum // 10) != (userNum % 10):
        print(userNum)
        userNum -= 1

    print(userNum) # After the loop, you still need to print the last number.