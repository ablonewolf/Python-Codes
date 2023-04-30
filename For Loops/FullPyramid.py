def draw_full_pyramid(level):
    draw_upper_pyramid(level)
    draw_lower_pyramid(level)


def draw_lower_pyramid(level):
    for line in reversed(range(1, level + 1)):
        for space in reversed(range(1, level - line + 1)):
            print("", end=" ")
        for item in reversed(range(1, line + 1)):
            if (item == 1):
                print("*")
            else:
                print("*", end=" ")


def draw_upper_pyramid(level):
    for line in range(1, level + 1):
        if (line == level):
            continue
        for space in reversed(range(1, level - line + 1)):
            print("", end=" ")
        for item in range(1, line + 1):
            if (item == line):
                print("*")
            else:
                print("*", end=" ")


level = int(input("Enter the level for full pyramid: "))
draw_full_pyramid(level)
