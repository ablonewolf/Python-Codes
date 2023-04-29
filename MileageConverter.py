MILE_TO_KILOMETER = 1.60934


def checkUserInput(kms):
    if (kms.isdigit()):
        print(f"You have travelled {kms} kilometers today: ")
        return True
    else:
        print("Invalid input. Please try again.")
        return False
# method to check whether the input is valid or not


def takeUserInput():
    kms = input("Enter how many kilometers you have travelled today: ")
    return kms
# method to take user input and return it


def convertToMile(kms):
    kms = float(kms)
    miles = kms / MILE_TO_KILOMETER
    return miles
# method to convert from kilometers to miles


while (1):
    kilometers = takeUserInput()
    if (checkUserInput(kilometers)):
        print(
            f"In miles, you have travelled {convertToMile(kilometers):.3f} distance.")
        break
