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
    score = 10
    expected_number = generate_random_number()
    number = take_input()
    while (play_game.want_to_play):
        if (number != None):
            if (number == expected_number):
                print("You have guessed it! You won!")
                print(f"Your score is {score}")
                score = 10
                number = 0
                choice = check_if_keep_playing()
                if (choice == 'n'):
                    print("Thanks for playing. Bye!")
                    play_game.want_to_play = False
                elif (choice == "y"):
                    play_game()
                else:
                    print("Invalid choice. Enter again")
                    choice = check_if_keep_playing()
            elif (number > expected_number):
                score -= 1
                number = take_input_if_higher()
            else:
                score -= 1
                number = take_input_if_lower()

        else:
            score -= 1
            number = take_input()


play_game.want_to_play = True
play_game()
