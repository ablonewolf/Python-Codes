import UnionAndIntersection


def main_menu():
    first_list = input("Enter the elements of the first list(Number of elements should be more than one): ")
    try:
        first_list = list((int(number) for number in first_list.split(" ")))
    except:
        first_list = None
    second_list = input("Enter the elements of the second list(Number of elements should be more than one): ")
    try:
        second_list = list((int(number) for number in second_list.split(" ")))
    except:
        second_list = None
    if first_list is not None and second_list is not None and len(first_list) > 1 and len(second_list) > 1:
        print(f"Union of the two lists is: {UnionAndIntersection.find_union(first_list, second_list)}")
        print(
            f"Intersection of the two lists is: {UnionAndIntersection.find_intersection(first_list, second_list)}"
        )
    else:
        print("Size of one or both of the lists are small or invalid values has been provided. Please try again.")
        main_menu()
        return
    return


main_menu()
