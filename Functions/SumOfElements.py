def sum_of_elements(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


def take_input():
    print("Enter numbers to calculate their sum or hit enter to exit providing input")
    numbers = input("Enter numbers: ")

    if len(numbers) == 0:
        return None
    else:
        numbers = tuple(int(item) for item in numbers.split(' ') if item != '')
        return numbers


def main_menu():
    numbers = take_input()
    print(f"The sum of {numbers} is: {sum_of_elements(*numbers)}")


main_menu()
