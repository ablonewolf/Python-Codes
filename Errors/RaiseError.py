colors = ('red', 'green', 'blue', 'black',
          'yellow', 'violet', 'purple', 'brown')


def color_the_text(text, color):
    if color not in colors:
        raise ValueError(f"{color} is not a valid color.")
    return f"{text} has been printed in color {color}"


def take_input():
    text = input("Enter the text you want to color: ")
    color = input("Enter the color: ")
    if (len(text) == 0 or len(color) == 0) or (text is None or color is None):
        print("Invalid Input. Please try again.")
        raise ValueError
    return text, color


def main_menu():
    text, color = take_input()
    color_the_text(text, color)


main_menu()
