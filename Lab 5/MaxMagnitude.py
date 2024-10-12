def max_magnitude(user_val1, user_val2, user_val3):
    # In this solution, I take three new variables to
    #   store the magnitudes of the three user_vals
    # We want to return the value that has the highest
    #   magnitude, not the magnitude itself
    # E.g. if -17 is the largest magnitued, then return
    #   -17, not 17
    absVal1 = abs(user_val1)
    absVal2 = abs(user_val2)
    absVal3 = abs(user_val3)

    # Compare each magnitude against the others
    # Return the original number
    if   (absVal1 > absVal2) and (absVal1 > absVal3):
        return user_val1
    elif (absVal2 > absVal1) and (absVal2 > absVal3):
        return user_val2
    elif (absVal3 > absVal2) and (absVal3 > absVal1):
        return user_val3
    
if __name__ == '__main__':
    # If you noticed, I did not name my input variables
    #   user_val1, user_val2, or user_val3.
    # You don't need to name these variables the same as
    #   your parameters, as long as they are the same data type
    #   (data types as in int, float, string, etc.)
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    # Here, I pass num1, num2, and num3 as the parameters 
    #   to the function.
    #   these variables become the respective variable used
    #   in the function
    #
    # num1 becomes user_val1
    # num2 becomes user_val2
    # num3 becomes user_val3
    print(max_magnitude(num1, num2, num3))