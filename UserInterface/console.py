from Domain.Vanzare import get_string, creeaza_carte, get_title, get_genre, get_price, get_sale
from Logic.ascending_sort_1 import asc_sort
from Logic.distinct_title_for_gen import show_distinct_number
from Logic.general_logic import create, update, delete, read
from Logic.min_price import get_min_price
from Logic.modify_genre import modify_g
from Logic.modify_prices import modify_prices
from Logic.undo_redo import do_undo, do_redo
from UserInterface.comand_line_console import command_line_console


def show_menu():
    print('1. CRUD')
    print('2. Reducere pret pentru clientii cu silver si gold.')
    print('3. Modificarea genului pentru un titlu dat.')
    print('4. Determinarea prețului minim pentru fiecare gen.')
    print('5. Ordonarea vanzarilor crescator dupa pret.')
    print('6. Afișarea numărului de titluri distincte pentru fiecare gen. ')
    print('u. Undo')
    print('r. Redo')
    print('c. Command line console')
    print('x. Exit')


def handle_add(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input("Dati id-ul vanzarii: "))
    except ValueError as ve:
        print('Eroare, id-ul introdus nu este un numar valid! Detalii: ', ve)
        return vanzari

    nume = input("Dati numele cartii ce urmeaza a fi pusa in vanzare: ")
    gen = input("Introduceti genul cartii: ")
    try:
        pret = float(input("Dati pretul cartii: "))
    except ValueError as ve:
        print('Eroare, nu ati introdus un pret valid! Detalii: ', ve)
        #pret = float(input("Dati pretul cartii: "))
        return vanzari
    reducere = input("Introduceti tipul cardului de fidelitate: ")
    return create(vanzari,id_vanzare, nume, gen, pret, reducere, undo_list, redo_list)


def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_string(vanzare))


def handle_update(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input("Dati id-ul vanzarii care se actualizeaza: "))
        nume = input("Dati noul nume al cartii ce urmeaza a fi pusa in vanzare: ")
        gen = input("Introduceti noul gen al cartii: ")
        pret = float(input("Dati noul pret al cartii: "))
        reducere = input("Introduceti tipul cardului de fidelitate: ")
        return update(vanzari, creeaza_carte(id_vanzare, nume, gen, pret, reducere), undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)

    return vanzari


def handle_delete(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input("Dati id-ul vanzarii care se va sterge: "))
        vanzari = delete(vanzari, id_vanzare, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare, ', ve)
    return vanzari


def handle_show_details(vanzari):
    id_vanzare = int(input("Dati id-ul vanzarii pentru care doriti detalii: "))
    vanzare = read(vanzari, id_vanzare)
    print(f'Titlul cartii: {get_title(vanzare)}')
    print(f'Genul cartii: {get_genre(vanzare)}')
    print(f'Pretul cartii: : {get_price(vanzare)}')
    print(f'Tipul reducerii: {get_sale(vanzare)}')


def handle_crud(vanzari, undo_list, redo_list):
    while True:
        try:
            print('1. Adaugare')
            print('2. Modificare')
            print('3. Stergere')
            print('a. Afisare')
            print('d. Detalii vanzare')
            print('b. Revenire')

            optiune = input('Optiunea aleasa: ')
            if optiune == '1':
                vanzari = handle_add(vanzari, undo_list, redo_list)
            elif optiune == '2':
                vanzari = handle_update(vanzari, undo_list, redo_list)
            elif optiune == '3':
                vanzari = handle_delete(vanzari, undo_list, redo_list)
            elif optiune == 'a':
                handle_show_all(vanzari)
            elif optiune == 'd':
                handle_show_details(vanzari)
            elif optiune == 'b':
                break
            else:
                print('Optiune invalida.')
        except Exception as ex:
            print('Eroare: ', ex)
    return vanzari


def handle_modify_genre(vanzari):
    try:
        to_modify = input("Dati tilul cartii a carui gen se doreste modificarea: ")
        genre_to_be_replaced_with = input("Introduceti noul gen al cartii")
        vanzari = modify_g(vanzari, to_modify, genre_to_be_replaced_with)
    except ValueError as ve:
        print('Eroare:', ve)
        return vanzari


def handle_ascending_sort(vanzari, undo_list, redo_list):
    sorted = asc_sort(vanzari, undo_list, redo_list)
    return sorted


def handle_command_console(vanzari, undo_list, redo_list):
    return command_line_console(vanzari, undo_list, redo_list)


def handle_undo(vanzari, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, vanzari)
    if undo_result is not None:
        return undo_result
    return vanzari


def handle_redo(vanzari, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, vanzari)
    if redo_result is not None:
        return redo_result
    return vanzari


def handle_get_min_price(vanzari):
    result = get_min_price(vanzari)
    for index in result:
        print(f'Pentru genul {index} , pretul minim este: {result[index]}')


def handle_count_distinct_title(vanzari):
    result = show_distinct_number(vanzari)
    for index in result:
        if result[index] == 1:
            print(f'Exista un singur titlu distinct pentru genul {index}')
        else:
            print(f'Exista {result[index]} titluri distincte pentru genul {index}')


def run_ui(vanzari, undo_list, redo_list):

    while True:
        handle_show_all(vanzari)
        try:
            show_menu()
            optiune = input('Optiunea aleasa: ')
            if optiune == '1':
                vanzari = handle_crud(vanzari, undo_list, redo_list)
            elif optiune == '2':
                vanzari = modify_prices(vanzari, undo_list, redo_list)
            elif optiune == '3':
                vanzari = handle_modify_genre(vanzari)
            elif optiune == '4':
                handle_get_min_price(vanzari)
            elif optiune == '5':
                vanzari = handle_ascending_sort(vanzari, undo_list, redo_list)
            elif optiune == '6':
                handle_count_distinct_title(vanzari)
            elif optiune == 'c':
                vanzari = handle_command_console(vanzari,undo_list, redo_list)
            elif optiune == 'u':
                vanzari = handle_undo(vanzari, undo_list, redo_list)
            elif optiune == 'r':
                vanzari = handle_redo(vanzari, undo_list, redo_list)
            elif optiune == 'x':
                break
            else:
                print('Optiune invalida.')
        except Exception as ex:
            print('Eroare: ', ex)

    return vanzari

