# Always keep your imports at the top of a file
# Under comments is fine as the compiler ignores comments
import math

x = float(input())
y = float(input())
z = float(input())


val1 = math.pow(x, z) # This reads as x^z
val2 = math.pow(x, math.pow(y, z)) # You can call methods inside methods
val3 = math.fabs(x - y) # You can write equations inside methods
val4 = math.pow(val1, 1/2) # Remember from math that a root is a power of 1/n
                           # Also remember to reuse variables where convenient!

print(f'{val1:.2f} {val2:.2f} {val3:.2f} {val4:.2f}')