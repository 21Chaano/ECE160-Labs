input_month = input()
input_day = int(input())

# This was one of the lab modules that stumped many people
# Just like Interstate Highway Numbers, there are many different solutions, some cleaner than others
# Below is my method, and I'll explain what is going on


validDay = False # Automatically assume that the user entered an invalid number for the day. We will need to double check it
# Here I have two lists, longMonth and shortMonth
# longMonth is a list of all months that have up to 31 days
# shortMonth is a list of all months that have up to 30 days
# Notice that February is not in any list. That is because it can only have a max of 29 days
longMonth  = ["January", "March", "May", "July", "August", "October", "December"]
shortMonth = ["April", "June", "September", "November"]

# These lists are all the months in each season, given by the module
# There are months that appear in multiple lists, but that's fine
# These months that appear multiple times are what I call "border months" 
# Border months are the months at the beginning or end of a season
spring = ["March", "April", "May", "June"]
summer = ["June", "July", "August", "September"]
autumn = ["September", "October", "November", "December"]
winter = ["December", "January", "February", "March"]

# Here is where we check to see if input_day is a valid day
if input_day < 1: # day cannot be 0 or negative
    validDay = False
if (input_month in longMonth) and (1 <= input_day <= 31): # Make sure that the month and day match (e.g. April 31 is not valid)
    validDay = True
elif (input_month in shortMonth) and (1 <= input_day <= 30): # If it's not a long month, it might be a short month
    validDay = True
elif (input_month == "February") and (1 <= input_day <= 29): # If it's not a long or short month, hopefully it's February
    validDay = True
else:
    print("Invalid") # If none of the above are true, print "Invalid" and because validDay is still False, none of the code below works

    
# Here we check to see which season the input month and day belong to
# Each of the 4 main branches follow the same pattern
# Check to see what season input_month belongs to
# Check to see if input_month is a "border month"
# If input_month is in fact a border month, then check if the day is in the date range provided
# If input month is not a border month, it still must be a month in that season, so we just need to validate that the day is good
# Remember that the "and" keyword only returns true if the connected conditionals are all true
# As stated earlier, none of this code will print anything if validDay is still False after the checks above
if input_month in spring:
    if (input_month == "March") and (20 <= input_day <= 31):
        print("Spring")
    elif (input_month == "June") and (1 <= input_day <= 20):
        print("Spring")
    elif (input_month != "March") and (input_month != "June") and validDay:
        print("Spring")

if input_month in summer:
    if (input_month == "June") and (21 <= input_day <= 30):
        print("Summer")
    elif (input_month == "September") and (1 <= input_day <= 21):
        print("Summer")
    elif (input_month != "June") and (input_month != "September") and validDay:
        print("Summer")
        
if input_month in autumn:
    if (input_month == "September") and (22 <= input_day <= 30):
        print("Autumn")
    elif (input_month == "December") and (1 <= input_day <= 20):
        print("Autumn")
    elif (input_month != "September") and (input_month != "December") and validDay:
        print("Autumn")
        
if input_month in winter:
    if (input_month == "December") and (21 <= input_day <= 31):
        print("Winter")
    elif (input_month == "March") and (1 <= input_day <= 19):
        print("Winter")
    elif (input_month != "December") and (input_month != "March") and validDay:
        print("Winter")
    