def find_intersection(first_collection, second_collection):
    return [item for item in first_collection if item in second_collection]


def find_union(first_collection, second_collection):
    union_list = first_collection + \
        [item for item in second_collection if item not in first_collection]
    return sorted(union_list)


def main_menu():
    n = int(input("Enter the size of the first list: "))
    print("Enter the elements of the first list.")
    first_collection = []
    i = 0
    while i < n:
        item = int(input())
        first_collection.append(item)
        i += 1
    n = int(input("Enter the size of the second list: "))
    print("Enter the elements of the second list.")
    second_collection = []
    i = 0
    while i < n:
        item = int(input())
        second_collection.append(item)
        i += 1
    print(
        f"Union of the two lists is: {find_union(first_collection, second_collection)}")
    print(
        f"Intersection of the two lists is: {find_intersection(first_collection, second_collection)}")


main_menu()
