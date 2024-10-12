user_text = input()

# This is another problem with multiple solutions. Below is how I solved it
count = len(user_text) # Start with the length of the entire input
invalidChar = [' ', ',', '.', '!'] # A list of the invalid characters according to the problem

# Again, you could also use a while-loop, I just find for-loops easier to handle
for i in range(len(user_text)):
    if user_text[i] in invalidChar:
        count -= 1 # If one of the user_text characters is an invalid character, decrement the count by 1

print(count)

# Another way you could solve this involves starting count at 0, 
#   then increasing it anytime you run into a *valid* character
#   don't change count when you reach an invalid character

# Here's an example of that solution:
#
# user_text = input()
# count = 0
# invalidChar = [' ', ',', '.', '!']
# 
# for i in range(len(user_text)):
#    if user_text[i] in invalidChar:
#        continue
#    else:
#        count += 1