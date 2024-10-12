num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

pro = num1 * num2 * num3 * num4
sum = num1 + num2 + num3 + num4
avg = sum / 4

print(f'{pro:.0f} {avg:.0f}') # This makes it so that there are no decimals visible
print(f'{pro:.3f} {avg:.3f}') # Goes to three decimal places

# You should not try to force a float to be an int. That may screw with the actual value