base_char = input()
head_char = input()

row1 = '      ' + head_char
''' Type your code here. '''
row2 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char
row3 = row2 + head_char # The difference between row2 and row3 is simply just an extra head_char.
                        # No need to add base_char over and over again

print(row1)
print(row2)
print(row3)
print(row2)
print(row1)

