Player2Total = 0
mul=1
End = False
FiveRounds = False
i = 4

with open('authnames.txt','r') as authnames: #open file
    lines = authnames.read().splitlines() #file to list

player1authentication = False
while player1authentication == False:
    player1name = input('Player 1, enter your name\n')
    player1name = player1name.lower()
    if player1name in lines:
        player1authentication = True
    else:
        print('You are not allowed to play')

player2authentication = False
while player2authentication == False:
    player2name = input('Player 2, enter your name\n')
    player2name = player2name.lower()
    if player2name == player1name:
        print('Your name is the same player 1')
    elif player2name in lines:
        player2authentication = True
    else:
        print('You are not allowed to play')

speed = input('How fast would you like the game to be (seconds between output)\n')
try:
    speed = float(speed)
except:
    print('You failed to provide an number, so the speed will be the default value of 0.5\n')
    speed = 0.5
time.sleep(speed)

def roll(PlayerName):
    random.seed()
    LocalScoreA = random.randrange(1,7)
    print(f'{PlayerName} rolled a {LocalScoreA}')
    time.sleep(speed)
    LocalScoreB = random.randrange(1,7)
    print(f'{PlayerName} rolled a {LocalScoreB}')
    time.sleep(speed)    
    LocalScore = LocalScoreA + LocalScoreB
    print(f'The total is {LocalScore}')
    time.sleep(speed)
    LocalScoreC = random.randrange(1,7)
    if LocalScoreA == LocalScoreB:
        LocalScore += LocalScoreC
        print(f'{PlayerName} rolled a double. {PlayerName} gets to roll an extra dice')
        time.sleep(speed)
        print(f'This was a {LocalScoreC}')
        time.sleep(speed)
        print(f'The score is now {LocalScore}')
        time.sleep(speed)
    if LocalScore % 2 == 0:
        LocalScore += 10
        print('The score is even, 10 points added')
    else:
        LocalScore -= 5
        print('The score is odd, 5 points subtracted')
    time.sleep(speed)
    if LocalScore < 0:
        print(f'The score of {LocalScore} is less than 0, so it will be set to 0')
        LocalScore = 0
        time.sleep(speed)
    print(f'{PlayerName}, you got {LocalScore}\n')
    time.sleep(speed)
    return(LocalScore)

def suddendeath(PlayerName):
    LocalScore = random.randrange(1,7)
    print(f'{PlayerName}, you got {LocalScore}\n')
    time.sleep(speed)
    return(LocalScore)

for i in range(5):
    print(f'--Round {i+1}--\n')
    time.sleep(speed)
    Player1Score = roll(player1name)
    Player2Score = roll(player2name)
    Player1Total += Player1Score
    Player2Total += Player2Score

    if i == 4:
        print('The 5 Rounds have ended')
        time.sleep(speed)
        print(f'Final totals:')
        time.sleep(speed)
    else:
        print(f'Running totals:')
    time.sleep(speed)
    print(f'    {player1name} - {Player1Total}')
    time.sleep(speed)
    print(f'    {player2name} - {Player2Total}\n')
    time.sleep(speed*mul)

while Player1Total == Player2Total:
    print('There is no winner, the game will go into sudden death mode\n')
    time.sleep(speed)
    print(f'Round --SUDDENDEATH--\n')
    time.sleep(speed)

    Player1Score = suddendeath(player1name)
    Player2Score = suddendeath(player2name)
    Player1Total += Player1Score
    Player2Total += Player2Score

    print(f'Final totals:')
    time.sleep(speed)
    print(f'    {player1name} - {Player1Total}')
    time.sleep(speed)
    print(f'    {player2name} - {Player2Total}\n')
    time.sleep(speed*3)

if Player1Total > Player2Total:
    print(f'{player1name} is the winner and will have their score written to the leaderboard if it makes the top 5\n')
    time.sleep(speed)
    with open('scores.txt','a') as scores: #open file
       scorelen = len(str(Player1Total))
       lines = scores.write(f'\n{Player1Total} - {player1name}')
else:
    print(f'{player2name} is the winner and will have their score written to the leaderboard\n')
    time.sleep(speed)
    with open('scores.txt','a') as scores: #open file
       lines = scores.write(f'\n{Player2Total} - {player2name}')
       scorelen = len(str(Player2Total))
       
with open('scores.txt','r') as scores: #open file
    lines = scores.read().splitlines() #file to list
   
lines.sort(key=lambda x: x[0:scorelen])
lines.reverse()
if len(lines) > 5:
    del lines[5:]

print('--High scores--\n')
time.sleep(speed)
for i in lines:
    print(i)
    time.sleep(speed)

with open('scores.txt','w') as scores: #open file
    scores.write('')
with open('scores.txt','a') as scores: #open file
    for i in lines:
        scores.write(i + '\n')
