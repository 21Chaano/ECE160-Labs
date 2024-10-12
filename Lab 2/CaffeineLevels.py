caffeine_mg = float(input())

# The pattern for this will be dividing caffeine_mg by exponentials of 2
# Every 6 hours, the level of caffeine will be half of what it was 6 hours ago
# If we start with  50mg of caffeine, it will be 25mg after 6hrs, 12.5mg after 12hrs, and 6.25mg after 18hrs
firstHalfLife  = caffeine_mg / 2
secondHalfLife = caffeine_mg / 4
fourthHalfLife  = caffeine_mg / 16 # Careful not to use 8. 24 hours would have experienced 4 half lifes, not 3

# We want to make sure that the numbers go to two decimal places, so we can make use of floating point percision
# To do this, we need to use string literals
print(f'After 6 hours: {firstHalfLife:.02f} mg') # The ":.02" will ensure that a max of two decimal places will be printed
print(f'After 12 hours: {secondHalfLife:.2f} mg') # You don't have to put ":.02f", ":.2f" will work the exact same way
print(f'After 24 hours: {fourthHalfLife:.2f} mg')