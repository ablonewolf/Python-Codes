for number in range(1, 21):
    if (number == 4 or number == 13):
        print(f"{number} is unlucky.")
    elif (number % 2 == 0):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
