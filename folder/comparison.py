name = input('enter ur name: ')
lenght = len(name)

if lenght <= 2:
    print(f'{name} is too short, min 3 characters')

elif lenght >= 50:
    print(f'{name} is too long, 50 characters max')

else:
    print(f"name: '{name}' lookin' good!")
