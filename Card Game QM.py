import random

deck = []
usedCards = []

suits = [.1, .2, .3, .4]
# .1 = Spades, .2 = Clubs, .4 = Diamonds, .4 = Hearts
ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# 1 = Ace, 11 = Jack, 12 = Queen, 13 = King

# Makes 52 "cards", a whole deck
for x in range(0,4):
    xd = suits[x]
    for y in range(0,13):
        cx = ranks[y]
        a = '{} of {}'.format(cx,xd)
        deck.append(a)

# Variables for comparison
p1Hand = ''
computerHand = ''

# Variable for scoring.
p1Score = 0
computerScore = 0

# Random Question just for the heck of it
PlayerOption = int(input('Play the Game? Yes or No? 1 for Yes and 2 for No. > '))

# Contructs a new function for the scoring system of the game.
def scoringSys():
    if computerScore > p1Score:
        print('Computer Wins!~')

    if p1Score > computerScore:
        print('You Win!~ Congratulations!~~')

    if computerScore == p1Score:
        print('Its a TIE! Congrats to both players!~')

while True:
    if PlayerOption == 1:
        ff = random.randrange(len(deck))
        p1Hand = deck[ff]
        usedCards.append(deck[ff])
        del deck [ff]
        print('Player Hand: ' + p1Hand)
        gg = random.randrange(len(deck))
        computerHand = deck[gg]
        usedCards.append(deck[gg])
        del deck[gg]
        print('Computer Hand: ' + computerHand)

        if p1Hand > computerHand:
            p1Score = p1Score + 1
            print('Player Score:' + str(p1Score))
            print('Computer Score:' + str(computerScore))

        elif computerHand > p1Hand:
            computerScore = computerScore + 1
            print('Player Score:' + str(p1Score))
            print('Computer Score: ' + str(computerScore))

        scoringSys()


    elif PlayerOption == 2:
        print('FeelsBadMan')
        break
    else:
        print('Invalid Response, Quitting Program.')
        break