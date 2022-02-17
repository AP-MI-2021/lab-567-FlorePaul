from Domain.Vanzare import get_price


def asc_sort(vanzari, undo_list, redo_list):
    undo_list.append(vanzari)
    redo_list.clear()
    return sorted(vanzari, key=get_price)

