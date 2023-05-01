from random import randint


def generate_random_number():
    return randint(1, 10)


def take_input():
    try:
        number = int(input("Guess a number between 1 and 10: "))
        return number
    except:
        print("Invalid input. Please try again")
        return None


def take_input_if_higher():
    print("Too high. Try again!")
    return take_input()


def take_input_if_lower():
    print("Too low. Try again!")
    return take_input()


def check_if_keep_playing():
    choice = input("Do you want to keep playing? (y/n): ")
    return choice.lower()


def play_game():
    want_to_play = True
    while (want_to_play):
        score = 10
        has_won = False
        expected_number = generate_random_number()
        number = take_input()
        while (not has_won):
            if (number == None):
                number = take_input()
            elif (score == 0):
                print("Sorry! You have lost the game.😞😞😞")
                print(f"Your score is zero.")
                choice = check_if_keep_playing()
                if (choice == 'n'):
                    print("Thanks for playing the game")
                    break
                elif (choice == 'y'):
                    score = 10
                    has_won = True
            else:
                if (number == expected_number):
                    print("Congrats! You win the game!😁😁😁")
                    print(f"Your score is {score}")
                    choice = check_if_keep_playing()
                    if (choice == 'n'):
                        has_won = True
                        want_to_play = False
                    elif (choice == 'y'):
                        score = 10
                        has_won = True
                elif (number > expected_number):
                    score -= 1
                    number = take_input_if_higher()
                else:
                    score -= 1
                    number = take_input_if_lower()


play_game()
