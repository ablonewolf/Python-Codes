def take_input():
    try:
        limit = int(input(
            "Enter the value of the limit upto which even or odd numbers will be printed: "))
        return limit
    except:
        print("Invalid value for the limit. Please try again.")
        return None


def print_even_numbers(limit):
    if (limit > 0):
        even_numbers = [num for num in range(1, limit + 1) if num % 2 == 0]
        if (len(even_numbers) > 0):
            print(f"Even numbers within {limit}:")
            for number in even_numbers:
                if (number == even_numbers[-1]):
                    print(number)
                else:
                    print(number, end=" ")
        else:
            print("No even numbers within that limit.")
    else:
        print("Value of the limit must be greater than 0")


def print_odd_numbers(limit):
    if (limit > 0):
        odd_numbers = [num for num in range(1, limit+1) if num % 2 == 1]
        if (len(odd_numbers) > 0):
            print(f"Odd numbers within {limit}:")
            for number in odd_numbers:
                if (number == odd_numbers[-1]):
                    print(number)
                else:
                    print(number, end=" ")
        else:
            print("No odd numbers within that limit")
    else:
        print("Value of the limit must be greater than 0")


def choice_input():
    choice = input(
        "Enter \'even\' if you want to print even numbers. Enter \'odd\' if you want to print odd numbers: ")
    return choice


def main_menu():
    limit = take_input()
    if (limit != None):
        while (True):
            choice = choice_input()
            if (choice.lower() == 'even'):
                print_even_numbers(limit)
                break
            elif (choice.lower() == 'odd'):
                print_odd_numbers(limit)
                break
            else:
                print("Invalid input as choice. Please try again")
    else:
        main_menu()


main_menu()
