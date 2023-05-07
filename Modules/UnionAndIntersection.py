find_intersection = lambda first_list, second_list: list(
    filter(lambda item: item in second_list, first_list))

find_union = lambda first_list, second_list: sorted(first_list + list(
    filter(lambda item: item not in first_list, second_list)))