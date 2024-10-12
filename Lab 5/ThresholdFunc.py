# We're used to seeing this in main
# Now we have a function dedicated to taking in user inputs
# It pretty much is the same as the other modules
def get_user_values():
    num_values  = int(input())
    user_values = []
    
    for i in range(num_values):
        user_values.append(int(input()))

    upper_threshold = int(input())

    # We want to return two separate values
    # Careful not to wrap in parentheses, that makes a tuple
    return user_values, upper_threshold

# Just like in Threshold.py from Lab 4, we use loops to make a new list
# Refer to Threshold.py for the code explanation
def ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    res_values = []
    for value in user_values:
        if value <= upper_threshold:
            res_values.append(value)
    
    return res_values

if __name__ == '__main__':
    user_values, upper_threshold = get_user_values()
    res_values = ints_less_than_or_equal_to_threshold(user_values, upper_threshold)
    
    for value in res_values:
        print(value)
