stroke    = int(input())
par       = int(input())
scoreName = "" # Initializing scoreName to an empty string. We'll use this variable later

# As per the requirements, the only valid pars are 3, 4, and 5
# The only valid score names are Eagle Birdie, Par, and Bogey
validPar = [3, 4, 5]
validScore = ["Eagle", "Birdie", "Par", "Bogey"]

# While you could use an if followed by elif's, sometimes it is easier to just use multiple if's
if (par - stroke) == 2:
    scoreName = "Eagle"
if (par - stroke) == 1:
    scoreName = "Birdie"
if par == stroke:
    scoreName = "Par"
if (stroke - par) == 1: # You could also do par - stroke for sake of consistency, just change the 1 to -1
    scoreName = "Bogey"

# These branches are just making sure that everything is valid, then print accordingly
if (par in validPar) and (scoreName in validScore):
    print(f'Par {par} in {stroke} strokes is {scoreName}')
else:
    print(f'Par {par} in {stroke} strokes is Error')