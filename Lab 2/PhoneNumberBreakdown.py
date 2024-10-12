phone_number = int(input())

# Floor division, //,  will return the quotient as the nearest integer rounded down
# If you use 10^x as your divisor (1, 10, 100, 1000, etc.) you will get all numbers to the left of where the zeros would be
# Ex. 151 // 10 = 15, 34789 // 1000 = 34

# The modulous operator will perform division between a dividend and divisor, but return the remainder
# If you use 10^x as your divisor (see above), then you will get all the numbers in the places of the zeros
# Ex. 1987 % 100 = 87, 1234567 % 100000 = 234566

areaCode = phone_number // 10000000 # We want to ignore the last 7 digits, but keep the first 3

# Use % to remove the area code, then // to remove the last 4 digits
middleThree = (phone_number % 10000000) // 10000
# middleThree = (phone_number // 1000) % 1000 is another solution
# This would remove the last 4 digits, then take the "new" last three digits

lastFour = phone_number % 10000

print(f'({areaCode}) {middleThree}-{lastFour}')

# Do note that the above code will not work if any of the parts of the phone number start with 0
# They will be ignored when the arithmetic operators return your result
# Ex. 8005570298 will return (800) 557-298 instead of (800) 557-0298