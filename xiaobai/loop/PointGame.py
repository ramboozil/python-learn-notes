import random


def roll_dice(times='3', points=None):
    print('<<<<<<<<<<<<<Start roll the dice>>>>>>>>>>')
    if points is None:
        points = []
    while times > 0:
        points.append(random.randrange(1, 7))
        times = times - 1
    return points


def isBigOrSmall(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'


def start_game():
    betCount = 1000
    print('*************Start The Game****************')
    choices = ['Big', 'Small']
    while betCount > 0:
        choice = input('Big or Small :')
        if choice in choices:
            bet = input('How much you wanna bet? -')
            points = roll_dice(3)
            total = sum(points)
            you_win = choice == isBigOrSmall(total)
            if you_win:
                print('Congratulations! The point is ' + str(points) + ' you win the game!')
                betCount = betCount + int(bet)
                print('you gained {} , you have {} now'.format(bet, betCount))
            else:
                print('Sorry ! The point is {}'.format(points) + ' you lost the game!')
                betCount = betCount - int(bet)
                print('you lost {} , you have {} now'.format(bet, betCount))
        else:
            print('Invalid input!')
            start_game()
    else:
        print('Game Over')


start_game()
