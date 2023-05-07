def check_character(char):
    return 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122


def multiple_letter_count(string):
    if len(string) == 0:
        return None
    return {letter.lower(): string.lower().count(letter.lower()) for letter in string if check_character(letter)}


def take_input():
    string = input("Enter the string: ")
    if len(string) == 0:
        print("Empty string not accepted. Please try again.")
    else:
        return string


def print_letter_count(dictionary):
    for (key, value) in dictionary.items():
        print(f"Count for {key}: {value}")


def main_menu():
    string = take_input()
    if string is None:
        main_menu()
    letter_count = multiple_letter_count(string)
    print_letter_count(letter_count)


main_menu()
