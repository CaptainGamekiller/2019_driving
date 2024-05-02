country = input('Where are you from? ')
age = input('Please enter your age: ')
age = int(age)
if country == 'Taiwan':
    if age >= 18:
        print('You are eligible for a driver\'s license.')
    else:
        print('You are not eligible for a driver\'s license.')
elif country == 'USA':
    if age >= 16:
        print('You are eligible for a driver\'s license.')
    else:
        print('You are not eligible for a driver\'s license yet.')
else:
    print('Please only enter Taiwan or USA.')
