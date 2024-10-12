# Similar to the smallest and largest problem,
#   this lab module tests taking in an unknown
#   number of inputs

# As per requirements, this is the first input
#   which will define the number of inputs that follow
maxLength = int(input())

nums = []
i = 0
# Unlike the above mentioned problem, implementing a
#   for-loop is just as easy
# Here, I still use a while-loop but I will attach an
#   alt-solution using a for-loop at the end of the code
while i in range(0, maxLength):
    # You can throw the input straight into the append()
    #   method without assigning the input to the variable
    nums.append(int(input()))
    i += 1

# After making the list, you still need that last input for the threshold
threshold = int(input())

# I'm using two while loops here, so I need a second iterator variable
# If you do reuse i, make sure to reset it to 0
j = 0
while j in range(0, len(nums)):
    if nums[j] <= threshold:
        # There is probably a way to do this in one line, but I couldn't think of it
        print(nums[j], end='')
        print(',', end='')
    j += 1
    

###################################################
# Alt-Solution:
#
# maxLength = int(input())
# 
# nums = []
# for i in range(maxLength):
#    nums.append(int(input()))
# 
# threshold = int(input())
# 
# for i in range(len(nums)):
#    if nums[i] <= threshold:
#        print(nums[i], end='')
#        print(',', end='')
#
###################################################
