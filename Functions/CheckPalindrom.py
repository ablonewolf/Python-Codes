def is_palindrome(string):
    is_palindrome = True
    last_index = -1
    for char in string:
        # print(char + " " + string[last_index])
        if (char == ' ' or string[last_index] == ' '):
            continue
        else:
            if (char.lower() == string[last_index].lower()):
                last_index = last_index - 1
            else:
                is_palindrome = False
                break

    return is_palindrome


def take_input():
    string = input("Enter the string to check whether it is a palindrome: ")
    if (len(string) > 0):
        return string
    else:
        print("Invalid input. Please try again.")
        return None


def main_menu():
    string = take_input()
    if (string == None):
        main_menu()
    else:
        palindrome = is_palindrome(string)
    if (palindrome):
        print(f"{string} is a palindrome string.")
    else:
        print(f"{string} is not a palindrome string.")


main_menu()
