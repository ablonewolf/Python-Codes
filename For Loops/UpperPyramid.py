def draw(level):
    for line in range(1, level + 1):
        for space in reversed(range(1, level - line + 1)):
            print("", end=" ")
        for item in range(1, line + 1):
            if (item == line):
                print("*")
            else:
                print("*", end=" ")


level = int(input("Enter the level for the upper pyramid: "))
draw(level)
