def is_sub_string(string, sub_string):
    return sub_string in string


def main_menu():
    string = input("Enter the main string: ")
    sub_string = input("Enter the sub string: ")
    if (len(string) > 0 and len(sub_string) > 0):
        if is_sub_string(string, sub_string):
            print(f"{sub_string} is a substring of {string}.")
        print(f"{sub_string} is not a substring of {string}.")
    else:
        print("Invalid input. Please try again.")
        main_menu()
