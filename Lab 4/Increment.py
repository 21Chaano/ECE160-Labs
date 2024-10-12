firstNum = int(input())
lastNum  = int(input())

# Check to see if the range is valid
if lastNum >= firstNum:
    for i in range(firstNum, lastNum + 1, 5): # this will increment from the first num to last num in steps of 5
        num = i # This is not really needed, you could just throw 'i' into the print statement instead
        print(num, end=' ') # We want all the numbers to be in one line, so make use of end=' '
    print()

else:
    print("Second integer can't be less than the first.")