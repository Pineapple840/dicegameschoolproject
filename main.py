with open('authnames.txt','r') as authnames: #open file
    lines = authnames.read().splitlines() #file to list

player1authentication = False
while player1authentication == False:
    player1name = input('Player 1, enter your name\n')
    if player1name in lines:
        player1authentication = True
    else:
        print('You are not allowed to play')

player2authentication = False
while player2authentication == False:
    player2name = input('Player 2, enter your name\n')
    if player2name == player1name:
        print('Your name is the same player 1')  
    elif player2name in lines:
        player2authentication = True
    else:
        print('You are not allowed to play')
