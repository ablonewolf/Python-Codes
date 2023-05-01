def take_input():
    try:
        number = int(
            input("Enter the number for which you want to print its numeric table: "))
        return number
    except:
        print("Invalid value please try again")
        return None


def print_numeric_table(number):
    i = 1
    for item in [number * multiplier for multiplier in range(1, 11)]:
        print(f"{number} * {i} = {item}")
        i += 1


def main_menu():
    number = take_input()
    if (number != None):
        print(f"The numeric table for {number} is given below:")
        print_numeric_table(number)
    else:
        main_menu()


main_menu()
