# This is the same problem as LeapYear.py from Lab 3
# See Lab 3, LeapYear.py for the explanation of how
#   the code works
# There are other things I will point out in this file
#   relevant mainly to the function version
def days_in_feb(user_year):
    isLeapYear = False
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                isLeapYear = True
        else:
            isLeapYear = True
    if isLeapYear:
        # Pay attention to the function requirements.
        # The requirements say to return a number
        # Do not return the final string
        return 29
    else:
        return 28

if __name__ == '__main__':
    user_year = int(input())
    # We had the function days_in_feb return a number
    # We will use that function call to say how many days
    #   will be in February for the input year
    print(f'{user_year} has {days_in_feb(user_year)} days in February.')