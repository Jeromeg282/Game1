rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
}


def player_stat():
    print('----------------------------')
    print('You are in the {}'.format(currentRoom))
    print('----------------------------')
    print(f'{exits}')


# start player in Great Hall
currentRoom = 'Great Hall'
player_move = ''


while currentRoom != 'Exit':
    while currentRoom == 'Great Hall':
        player_stat()
        player_move = input('Enter your move:\n')
        if player_move not in ['South', 'south', 'Exit', 'exit']:
            print('Invalid move.')
        elif player_move in ['Exit', 'exit']:
            currentRoom = 'Exit'
            print('Play again soon!')
        elif player_move in ['South', 'south']:
            currentRoom = 'Bedroom'
    while currentRoom == 'Bedroom':
        player_stat()
        player_move = input('Enter your move:\n')
        if player_move not in ['North', 'north', 'East', 'east', 'Exit', 'exit']:
            print('Invalid move.')
        elif player_move in ['Exit', 'exit']:
            currentRoom = 'Exit'
            print('Play again soon!')
        elif player_move in ['North', 'north']:
            currentRoom = 'Great Hall'
        elif player_move in ['East', 'east']:
            currentRoom = 'Cellar'
    while currentRoom == 'Cellar':
        player_stat()
        player_move = input('Enter your move:\n')
        if player_move not in ['West', 'west', 'Exit', 'exit']:
            print('Invalid move.')
        elif player_move in ['Exit', 'exit']:
            currentRoom = 'Exit'
            print('Play again soon!')
        elif player_move in ['West', 'west']:
            currentRoom = 'Bedroom'