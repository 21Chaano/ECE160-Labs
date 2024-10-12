# Another unit conversion problem
# Very similar to DrivingCost, LapsToMiles, or StepCounter
def jiffies_to_seconds(user_jiffies):
    seconds = user_jiffies / 100
    return seconds

if __name__ == '__main__':
    jiffies = float(input())
    seconds = jiffies_to_seconds(jiffies)

    # This time, the requirement is to round to 3 places
    print(f'{seconds:.3f}')