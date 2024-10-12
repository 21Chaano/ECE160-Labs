# This loop will be infinite as long as there is no break statement
# Be VERY careful when doing something like this
while True:
    text = input()

    # This conditional here will break out of the while True loop if any of the conditions are met
    if text == 'Done' or text == 'done' or text == 'd':
        break

    i = len(text) - 1 # I am using a second while-loop, so I need to set my iterator variable manually
    phrase = '' # At the end of the loop, this should be the reversed string

    # In the first iteration of this second while-loop, i should be equal to the last index of the input text
    # At the last iteration, i should be 0
    while i >= 0:
        phrase = phrase + text[i]
        i -= 1

    print(phrase)