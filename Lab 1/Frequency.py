import math

f0 = int(input()) # This should be the basic frequency
r  = math.pow(2, 1/12) # Follows from MathFunctions.py

f1 = f0 * math.pow(r, 1) # Could just write this line as f1 = f0 * r
f2 = f0 * math.pow(r, 2)
f3 = f0 * math.pow(r, 3)

print(f'{f0:.2f} Hz')
print(f'{f1:.2f} Hz')
print(f'{f2:.2f} Hz')
print(f'{f3:.2f} Hz')