from keyword import iskeyword


def contains_keyword(*args):
    return all(arg for arg in args if type(arg) is str) and any(arg for arg in args if iskeyword(arg))


def take_input():
    string = input("Enter the string to check if it contains a keyword(it should be a string of more than one word): ")
    string = tuple(string.split(" "))
    if len(string) > 1:
        return string
    else:
        print("Invalid input. Please try again.")
        return None


def main_menu():
    string = take_input()
    if string is not None:
        if contains_keyword(*string):
            print(f"This string contains some built-in keywords of python")
        else:
            print(f"This string does not contain any keyword of python.")
    else:
        main_menu()
        return


main_menu()
