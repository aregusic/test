
is_running = True

while is_running == True:
    input1 = input('> ').lower()
    if input1 == 'help':
        print('''
        start - start the engine
        stop - stop the engine
        quit - exit the game''')

    elif input1 == 'start':
        print('Engine started!')

    elif input1 == 'stop':
        print('Engine stopped!')

    elif input1 == 'quit':
        print('Quitting game...')
        break
    else:
        print("Can't understand...")
    
   