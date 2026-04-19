def move_zeros(lst):
    for elem in lst:
        if elem == 0:
            lst.append(lst.pop(lst.index(elem)))
        else:
            continue
    return lst