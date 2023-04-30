import random

print('...rock...')
print('...paper...')
print('...scissors...')

options = ['rock', 'paper', 'scissors']


def takeInputs():
    player_1_choice = input('Player 1 chooses: ')
    if (player_1_choice not in options):
        return None, None
    else:
        computer_choice = options[random.randint(0, 2)]
        print(f'Computer chosses: {computer_choice}')
        return player_1_choice, computer_choice


def determineWinner(choice_1, choice_2):

    if (choice_1.lower() == 'rock' and choice_2.lower() == 'paper'):
        print('SHOOT!')
        print('Computer wins')
    elif (choice_1.lower() == 'scissors' and choice_2.lower() == 'rock'):
        print('SHOOT!')
        print('Computer wins')
    elif (choice_1.lower() == 'paper' and choice_2.lower() == "scissors"):
        print('SHOOT!')
        print('Computer wins')
    elif (choice_1.lower() == choice_2.lower()):
        print('It\'s a tie!')
    else:
        print('SHOOT!')
        print('You win.')


def game():
    while (True):
        choice_1, choice_2 = takeInputs()
        if ((choice_1 is not None and choice_2 is not None) and (choice_1.lower() in options and choice_2.lower() in options)):
            determineWinner(choice_1, choice_2)
            break
        else:
            print('Invalid choice as inputs. Please try again')


game()
