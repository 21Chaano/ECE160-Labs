def is_list_mult10(my_list):
    # Notice the wording in this for-loop
    # Rather than for i in range(),
    #   I use for num in my_list
    # What this does is rather than using
    #   an iterator variable to index,
    #   you can just take each element itself
    # We can do this because we are iterating
    #   through a list from start to end
    for num in my_list:
        # The moment we find a number that is NOT
        #   a multiple of 10, we want to exit
        if num % 10 != 0:
            return False
    # If we pass through the entire loop,
    #   that means all numbers are
    #   multiples of 10
    return True

# Almost a carbon copy of is_list_mult10(),
#   just with one key difference
def is_list_no_mult10(my_list):
    for num in my_list:
        # The moment we find a number that is
        #   a multiple of 10, we want to exit
        if num % 10 == 0:
            return False
    return True

if __name__ == '__main__':
    # Take in a certain amount of inputs similar to how
    #   we have done in previous problems
    listLength = int(input())
    numList    = []

    for i in range(listLength):
        numList.append(int(input()))

    if is_list_mult10(numList):
        print('all multiples of 10')
    elif is_list_no_mult10(numList):
        print('no multiples of 10')
    else: # If both are false, then it's mixed
        print('mixed values')