# Usually the Fibonacci Sequence is used to teach recursive functions
# It is still possible to implement without recursion
# You will all probably see this problem again in several chapters

# The Fibonacci Sequence is a mathematical sequence where the nth 
#   element in the sequence is the sum of the previous two elements
# The 0th and 1st element will be 0 and 1 respectively as they don't
#   have two elements that come before them
# The Fibonacci Sequence is as follows:
#   0, 1, 1, 2, 3, 5, 8, 13, 21, ...
def fibonacci(n):
    # If n is negative, that's a no-no
    if n < 0:
        return -1  
    # As mentioned above, this is a base case  
    if (n == 0):
        return 0
    # I include 2 in here because it's previous two elements
    #   are 0 and 1, meaning the 2nd element is 0 + 1 = 1
    if (n == 1) or (n == 2):
        return 1
    
    # I initialize a list to represent the sequence
    # The list starts with the base cases, then the for-loop serves
    #   to add more elements up to the nth element in the sequence
    sequence = [0, 1]
    # Start with 2 because we need already have 0 and 1
    for i in range(2, n + 1):
        # Negative indexing starts from the end of a string or list
        # -1 starts at the end, -2 starts at the second-to-last, and so on
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    # After we have the entire sequence, we only really care about
    #   the last element in the sequence
    return sequence[-1]



if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')