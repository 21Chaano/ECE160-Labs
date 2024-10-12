# This is a combo of Lab 4's ReverseBinary and StringReverse
# Here they are in function form

# This function takes an integer value and will
#   convert it to a reversed binary string
def int_to_reverse_binary(integer_value):
    # Initialize an empty string that we will
    # modify then return
    revBin = ''

    # This while loop is similar to the one used in
    # ReverseBinary.py from lab 4
    # If you use ">=" instead of ">" You will get an infinite loop
    # This is because 0 // 2 will always be 0
    while integer_value > 0: 
        # In Python, you can force data types
        # You can't add an int to a string,
        #   so I force integer_value to be a string
        revBin += str(integer_value % 2)
        # Remember to iterate else you will be 
        #   stuck in an infinite loop
        integer_value = integer_value // 2
    
    return revBin

# This function takes a string as an input
# The function will reverse the string and return
def string_reverse(input_string):
    # Initialize an empty string to modify and return
    reversedString = ''

    # This for-loop iterates from 0 to the length of the string
    for i in range(len(input_string)):
        # We want to reverse the string, so start from the 
        #   end of input_string
        # (-1 - i) will iterate as (-1 - 0), (-1 - 1), (-1 - 2), etc.
        reversedString += input_string[-1 - i]
    
    return reversedString

if __name__ == '__main__':
    userInt     = int(input())
    reversedBin = int_to_reverse_binary(userInt)
    userBin     = string_reverse(reversedBin)

    print(userBin)