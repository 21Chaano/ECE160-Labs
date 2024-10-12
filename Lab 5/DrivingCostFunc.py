# This is the same problem as a previous lab module, now in function form
# Refer to Lab 1, DrivingCost.py for code explanation
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    totalCost = dollars_per_gallon * (miles_driven / miles_per_gallon)
    return totalCost

if __name__ == '__main__':
    mileage       = float(input())
    costPerGallon = float(input())

    print(f'{driving_cost(mileage, costPerGallon,  10):.2f}')
    print(f'{driving_cost(mileage, costPerGallon,  50):.2f}')
    print(f'{driving_cost(mileage, costPerGallon, 400):.2f}')
