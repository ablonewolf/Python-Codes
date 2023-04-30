def draw(level):
    for line in range(1, level + 1):
        for item in range(1, line + 1):
            if (item == line):
                print("*")
            else:
                print("*", end="  ")


level = input("Enter the level of the lower left triangle: ")
draw(int(level))
