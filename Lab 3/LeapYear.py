is_leap_year = False
   
input_year = int(input())

if (input_year % 4) == 0: # Check if the year is evenly divisible by 4
    if (input_year % 100) == 0: # Check if it is a cenutry
        if (input_year % 400) == 0: # If it is a century, then it must be evenly divisible by 400
            is_leap_year = True
        else:
            is_leap_year = False
    else: # If the year is not divisible by 100, that's okay, we already saw it's divisible by 4
        is_leap_year = True
else:
    is_leap_year = False
    
# These print statements could also go into the above branches, though you wouldn't be making use of the boolean
if is_leap_year:
    print(f'{input_year} - leap year')
else:
    print(f'{input_year} - not a leap year')