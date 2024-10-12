totalChange = int(input())

# A quick check to see if we even have to make change
if totalChange == 0:
    print("No change")

# Number of dollars
# In order to even consider dollar coins, we need to check if we even have enough for that
if totalChange >= 100:
    dollars = totalChange // 100 # If totalChange is 100+, // returns how many full multiples of 100 there are
    totalChange = totalChange % 100 # We have the number of dollars, so now we make sure they aren't considered anymore.
    # Remember that % returns the remainder, so this is how we will need to update totalChange
    if dollars == 1: # Quick check for singular or plural
        print(f"{dollars} Dollar")
    else:
        print(f"{dollars} Dollars")
else: # Honestly I don't think this else statement is needed, but it is good for clarity
    dollars = 0

# All other coin types follow the same pattern, just uses different numbers for the value of the coins

# Number of quarters
if totalChange >= 25:
    quarters = totalChange // 25
    totalChange = totalChange % 25
    if quarters == 1:
        print(f"{quarters} Quarter")
    else:
        print(f"{quarters} Quarters")
else:
    quarters = 0

# Number of dimes
if totalChange >= 10:
    dimes = totalChange // 10
    totalChange = totalChange % 10
    if dimes == 1:
        print(f"{dimes} Dime")
    else:
        print(f"{dimes} Dimes")
else:
    dimes = 0

# Number of nickels
if totalChange >= 5:
    nickels = totalChange // 5
    totalChange = totalChange % 5
    if nickels == 1:
        print(f"{nickels} Nickel")
    else:
        print(f"{nickels} Nickels")
else:
    nickels = 0

# Number of pennies
if totalChange >= 1:
    pennies = totalChange // 1
    if pennies == 1:
        print(f"{pennies} Penny")
    else:
        print(f"{pennies} Pennies")
else:
    pennies = 0
