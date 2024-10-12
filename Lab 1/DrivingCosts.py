gasMileage = float(input())
gasCost    = float(input())

# This module's main goal is to teach floats and floating point precision
# The actual math problem itself is a unit conversion problem,
#   which engineers should be able to do
# 
# The final answer should only be in units of dollars
# Our inputs are in units of miles/gallon and dollars/gallon
# We also are given three different values as miles
#
# This solution is the unit conversion as follows:
#   dollars = (dollars/gallon) * (miles / (miles/gallon))
mile20  = gasCost * (20  / gasMileage)
mile75  = gasCost * (75  / gasMileage)
mile500 = gasCost * (500 / gasMileage)

print(f'{mile20:.2f} {mile75:.2f} {mile500:.2f}')