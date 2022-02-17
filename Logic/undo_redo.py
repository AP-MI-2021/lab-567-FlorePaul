def do_undo(undo_list: list, redo_list: list, current_list: list):
    """
    Executa un pas de undo
    :param undo_list: Lista de asteptare a pasilor de undo
    :param redo_list: O lista ce se va umple pe masura ce se efectueaza undo
    :param current_list: Lista curenta
    :return:
    """
    if undo_list:
        redo_list.append(current_list)
        return undo_list.pop()
    return []


def do_redo(undo_list: list, redo_list: list, current_list: list):
    """
    Executa un pas de redo
    :param undo_list: O lista ce se va umple pe masura ce se efectueaza redo
    :param redo_list: Lista de asteptare a pasilor de redo
    :param current_list: Lista curenta
    :return:
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo

    return []
