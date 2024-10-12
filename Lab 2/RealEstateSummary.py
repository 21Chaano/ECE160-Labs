current_price = int(input())
last_months_price = int(input())

priceDifference = current_price - last_months_price
monthlyMortgage = (current_price * 0.051) / 12

# Integers can be positive or negative. If a test expects a negative output, don't force
#   the negative sign. The variable will already be negative if it works out
print(f'This house is ${current_price}. The change is ${priceDifference} since last month.')
print(f'The estimated monthly mortgage is ${monthlyMortgage:.02f}')