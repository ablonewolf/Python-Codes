import random

options = ('rock', 'paper', 'scissors')
for option in options:
    print(f"...{option}...")

# method to take inputs


def takeInputs():
    player_1_choice = input('Player 1 chooses: ')
    if (player_1_choice.lower() not in options):
        return None, None

    computer_choice = options[random.randint(0, 2)]
    print(f'Computer chosses: {computer_choice}')
    return player_1_choice, computer_choice

# method to determine the winner of the round


def determineWinner(choice_1, choice_2):
    if (choice_1.lower() == 'rock' and choice_2.lower() == 'paper'):
        print('SHOOT!')
        print('Computer wins this round.')
        determineWinner.computer_score += 1
        return True
    elif (choice_1.lower() == 'scissors' and choice_2.lower() == 'rock'):
        print('SHOOT!')
        print('Computer wins this round.')
        determineWinner.computer_score += 1
        return True
    elif (choice_1.lower() == 'paper' and choice_2.lower() == "scissors"):
        print('SHOOT!')
        print('Computer wins this round.')
        determineWinner.computer_score += 1
        return True
    elif (choice_1.lower() == choice_2.lower()):
        print('It\'s a tie!')
        return False

    print('SHOOT!')
    print('You win this round.')
    determineWinner.player_score += 1
    return True


def game():
    print("The game will be played in a round of 3. If it's a tie, it won't be considered a round.")
    determineWinner.computer_score = 0
    determineWinner.player_score = 0
    # check whether the number of games played is less than 3 and both of the scores are less than 2. if not, we found a winner
    while (game.no_of_plays < 3 and (determineWinner.player_score < 2 and determineWinner.computer_score < 2)):
        choice_1, choice_2 = takeInputs()
        if ((choice_1 is not None and choice_2 is not None) and (choice_1.lower() in options and choice_2.lower() in options)):
            if (determineWinner(choice_1, choice_2)):
                game.no_of_plays += 1
        else:
            print('Invalid choice as inputs. Please try again')
    if (determineWinner.computer_score > determineWinner.player_score):
        print("Computer wins the game. Better luck next time 😥.")
    else:
        print("Congrats! You win the game😁😁😁")


game.no_of_plays = 0
game()
