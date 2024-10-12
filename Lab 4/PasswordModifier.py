word = input()
password = '' # We can't change what the input string is, so we use an empty string that we can change

# Iterate within the range from 0 to the length of your input string
# We check each and every character to see if it needs to be changed
# In each iteration, we need to add a character to password
for i in range(len(word)):
    if word[i] == 'i':
        password = password + '1'
    elif word[i] == 'a':
        password = password + '@'
    elif word[i] == 'm':
        password = password + 'M'
    elif word[i] == 'B':
        password = password + '8'
    elif word[i] == 's':
        password = password + '$'
    else:
        password = password + word[i] # If the character isn't one of the specified, add it to the new password
        
password = password + '!' # The password ends with !

print(password)