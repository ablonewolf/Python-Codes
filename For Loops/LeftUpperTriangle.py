def draw(level):
    for line in reversed(range(1, level + 1)):
        for item in range(1, line + 1):
            if (item == line):
                print("*")
            else:
                print("*", end="  ")


level = int(input("Enter the level for the Left Upper Triangle: "))
draw(level)
