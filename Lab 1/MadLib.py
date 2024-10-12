first_name = input()

whole_number     = int(input())
plural_noun      = input()
generic_location = input()

# In a print statement, you can interweave variables and strings 
# Do keep in mind that a comma will become a space
# Ex) for first_name       = Chansen
#         whole_number     = 24
#         plural_noun      = burgers
#         generic_location = McDonald's
#   The output will be:
#       "Chansen buys 24 different types of burgers at McDonald's"
print(first_name, 'buys', whole_number, 'different types of', plural_noun, 'at', generic_location)