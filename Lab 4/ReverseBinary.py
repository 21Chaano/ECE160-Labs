decNum = int(input())
revBin = [] # An empty list to use later

# When it comes to looping, there will almost always be a way to solve the problem with either a for-loop or while-loop
# I typically find for-loops to generally be easier, but there may be some cases where a while loop is better
# If you use a while-loop, remember to update your iterator so that you don't get caught in an infinite loop
while decNum > 0: # decNum is the "iterator" for this conditional
    bit = decNum % 2
    revBin.append(bit) # Store the bit in revBin list
    decNum = decNum // 2 # update decNum so that decNum will eventually use 

for i in range(len(revBin)): # i is the iterator, but we don't have to iterate it ourselves because the for-loop takes care of that
    print(revBin[i], end="")

print() # This is so that ZyBooks doesn't yell at us for not having a newline