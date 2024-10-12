# Define your function here.
def swap_values(user_val1, user_val2, user_val3, user_val4):
    # You can perform swaps by storing one value in a temporary
    #   variable before overwriting the initial variable
    # Here I use two temp variables, but you can probably use one

    # user_val1 is stored in temp1, user_val2 overwrites user_val1
    #   then finally, overwrite user_val2 with the value stored in temp1
    temp1 = user_val1
    user_val1 = user_val2
    user_val2 = temp1
    
    temp2 = user_val3
    user_val3 = user_val4
    user_val4 = temp2
    
    # In Python, you can return multiple values, as long as they are 
    #   separated by commas
    # Do not wrap these in parentheses, otherwise you will return a tuple
    return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__': 
    user_val1 = int(input())
    user_val2 = int(input())
    user_val3 = int(input())
    user_val4 = int(input())
    
    # If a function returns multiple values, you must assign each return value to
    #   its own variable, each separated by a comma
    newVal1, newVal2, newVal3, newVal4 = swap_values(user_val1, user_val2, user_val3, user_val4)
    
    print(newVal1, newVal2, newVal3, newVal4)


########################################################################
#
# Alt Solution:
#
# In this solution, I don't use any temp variables. You can simply
# return the user_vals in the swapped order
#
# def swap_values(user_val1, user_val2, user_val3, user_val4):
#    return user_val2, user_val1, user_val4, user_val3
#
# if __name__ == '__main__':
#    val1 = int(input())
#    val2 = int(input())
#    val3 = int(input())
#    val4 = int(input())
#    
#    new1, new2, new3, new4 = swap_values(val1, val2, val3, val4)
#
#    print(new1, new2, new3, new4)
#
########################################################################