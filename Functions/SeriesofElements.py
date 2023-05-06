def take_input():
    numbers = input("Enter atleast 3 numbers: ")
    try:
        numbers = tuple(int(number) for number in numbers.split(" "))
    except:
        numbers = None

    if (numbers is None):
        print("Invalid input. Please try again")
        return None
    elif (len(numbers) <= 2):
        print(
            "Please enter at least 3 numbers. Terminating operation. Please try again."
        )
        return None
    else:
        return numbers


def print_numbers(numbers):
    for num in numbers:
        if num == numbers[-1]:
            print(num)
        else:
            print(num, end=" ")


def square_of_series(numbers):
    return tuple(map(lambda x: x**2, numbers))


def cube_of_series(numbers):
    return tuple(map(lambda x: x**3, numbers))


def power_of_series(numbers, power):
    return tuple(map(lambda x: x**3, numbers))


def main_menu():
    numbers = take_input()
    if (numbers is None):
        main_menu()
        return
    while True:
        try:
            power = int(
                input(
                    "Enter the value of the power(It should be greater than zero and an integer): "
                ))
            if (not power > 0):
                print("Power should be greater zero. Please try again.")
                continue
            elif (power == 1):
                print_numbers(numbers)
                break
            elif (power == 2):
                print_numbers(square_of_series(numbers))
                break
            elif (power == 3):
                print_numbers(cube_of_series(numbers))
                break
            else:
                print_numbers(power_of_series(numbers, power))
                break
        except:
            print("Invalid input for power. Please try again.")
            continue


main_menu()
