to_do_list = []
print("Enter an item to add to your to-do list, or q to quit and show the items.")
while (True):
    item = input("Item: ")
    if (item.lower() == 'q'):
        if (len(to_do_list) == 0):
            print("You have an empty to-do list")
        else:
            print("The items in your to-do list are given below.")
            for list_item in to_do_list:
                if (list_item == to_do_list[-1]):
                    print(list_item)
                else:
                    print(list_item, end=", ")
        break
    else:
        to_do_list.append(item)
