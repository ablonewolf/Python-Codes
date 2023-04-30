print('...rock...')
print('...paper...')
print('...scissors...')

options = ['rock', 'paper', 'scissors']


def takeInputs():
    player_1_choice = input('(enter Player 1\'s choice): ')
    i = 0
    while (i < 10):
        print('****** NO CHEATING ******')
        print()
        i += 1
    player_2_choice = input('(enter Player 2\'s choice): ')
    return player_1_choice, player_2_choice


def determineWinner(choice_1, choice_2):

    if (choice_1.lower() == 'rock' and choice_2.lower() == 'paper'):
        print('SHOOT!')
        print('player2 wins')
    elif (choice_1.lower() == 'scissors' and choice_2.lower() == 'rock'):
        print('SHOOT!')
        print('player2 wins')
    elif (choice_1.lower() == 'paper' and choice_2.lower() == "scissors"):
        print('SHOOT!')
        print('player2 wins')
    else:
        print('SHOOT!')
        print('player1 wins')


def game():
    while (True):
        choice_1, choice_2 = takeInputs()
        if ((choice_1 is not None and choice_2 is not None) and (choice_1.lower() in options and choice_2.lower() in options)):
            determineWinner(choice_1, choice_2)
            break
        else:
            print('Invalid choice as inputs. Please try again')


game()
