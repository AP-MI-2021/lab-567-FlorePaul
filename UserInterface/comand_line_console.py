from Domain.Vanzare import get_string
from Logic.general_logic import create, delete


def command_line_console(vanzari, undo_list, redo_list):
    """
    Executa programul, sub forma de linie de comanda
    :param vanzari: lista de vanzari
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return: o noua lista prelucrata, in functie de comenzile introduse
    """
    # add, 1, Name, Gen, Price, Type
    command_line_str = input('Introduceti comanda: ')
    command_line = []
    command_line_str_split = command_line_str.split(', ')
    for index in command_line_str_split:
        command_line.append(index)
    for index in range(0, len(command_line)):
        if command_line[index] == 'add':
            try:
                vanzari = create(vanzari, int(command_line[index + 1]), command_line[index + 2],
                                 command_line[index + 3], float(command_line[index + 4]), command_line[index + 5],
                                 undo_list, redo_list)
            except ValueError as ve:
                print('Eroare! Detalii: ', ve)
        elif command_line[index] == 'showall':
            for vanzare in vanzari:
                print(get_string(vanzare))
        elif command_line[index] == 'delete':
            try:
                vanzari = delete(vanzari, int(command_line[index + 1]), undo_list, redo_list)
            except ValueError:
                print('Id-ul introdus nu exista, se va trece peste!')
    return vanzari
