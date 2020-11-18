def find_my_list(all_lists1, my_list):
    for index1, lst in enumerate(all_lists1):
        # Change the next line
        if id(lst) == id(my_list):
            return index1
    return None
