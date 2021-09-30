weight = input("What's your weight: ")
unit = input('(L)bs or (K)g: ')

if unit == 'L' or 'l':
    print(f'{float(weight) * 2.2} Kg')

elif unit == 'K' or 'k':
    print(f'{float(weight) / 2.2} Lbs')