def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup.get(kwargs.get('operation'), 0)

    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = f"{kwargs.get('message','The result is')} {int(operation_value)}"

    return final


def take_input():
    a, b = 0, 0
    try:
        a, b = map(int, input(
            "Enter the two numbers to perform operation: ").split(' '))
    except:
        print("Invalid input. Please try agian")
        return None
    operation = input(
        "Enter the desired operation(add for additon, subtract for subtraction, multiply for multiplication, divide for division): ")
    if not (operation.lower() == 'add' or operation.lower() == 'subtract' or operation.lower() == 'multiply' or operation.lower() == 'divide'):
        print("Invalid operation. Please try again")
        return None
    else:
        operation = operation.lower()
    is_float = input(
        "Enter true if you want the results in float or false if you want it in integer: ")
    if (is_float.lower() == 'false'):
        is_float = False
    elif (is_float.lower() == 'true'):
        is_float = True
    else:
        print("Invalid choice. Please try again")
        return None
    message = input(
        "Enter a message if you want it to be added with the result or hit enter to continue: ")
    arguments = {'make_float': is_float, 'first': a,
                 'second': b, 'message': message, 'operation': operation}
    return arguments


def main_menu():
    print("*** Welcome to console calculator ***")
    while True:
        arguments = take_input()
        if (arguments != None):
            result = calculate(**arguments)
            print(result)
            print("Do you wish to continue? y/n")
            option = input()
            if (option.lower() == "n"):
                print("Thanks for using our application. Have a nice day")
                break
            else:
                continue


main_menu()
