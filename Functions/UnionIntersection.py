find_intersection = lambda first_list, second_list: list(
    filter(lambda item: item in second_list, first_list))

find_union = lambda first_list, second_list: sorted(first_list + list(
    filter(lambda item: item not in first_list, second_list)))


def main_menu():
    n = int(input("Enter the size of the first list: "))
    print("Enter the elements of the first list.")
    first_list = []
    i = 0
    while i < n:
        item = int(input())
        first_list.append(item)
        i += 1
    n = int(input("Enter the size of the second list: "))
    print("Enter the elements of the second list.")
    second_list = []
    i = 0
    while i < n:
        item = int(input())
        second_list.append(item)
        i += 1
    print(f"Union of the two lists is: {find_union(first_list, second_list)}")
    print(
        f"Intersection of the two lists is: {find_intersection(first_list, second_list)}"
    )


main_menu()
