def draw(level):
    for line in range(1, level + 1):
        for item in range(1, level - line + 1):
            print("  ", end="")
        for item in reversed(range(1, line + 1)):
            if (item == 1):
                print("*")
            else:
                print("*", end=" ")


level = int(input("Enter the level for the lower right triangle: "))
draw(level)
