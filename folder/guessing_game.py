secret_number = 9
number_of_tries = 0
ges_limit = 5

while number_of_tries < ges_limit:
    guess = int(input('Guess the number: '))
    number_of_tries += 1
    if number_of_tries == 4:
        print(f'sorry, you failed to guess the number, it was {secret_number}')
        break
    elif guess == secret_number:
        print(f'You win! Number was {secret_number}')
        break
