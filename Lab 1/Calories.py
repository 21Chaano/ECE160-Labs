''' Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368 '''

age    = int(input())
weight = int(input())
bpm    = int(input())
mins   = int(input())

# When writing out long equations like this, it is a good idea to space out the 
#   variables and operators for sake of visual clarity
calories = ((age * 0.2757) + (weight * 0.03295) + (bpm * 1.0781) - 75.4991) * mins / 8.368

print(f'Calories: {calories:.2f} calories')