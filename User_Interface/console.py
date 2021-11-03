from Domain.cheltuieli import creeaza_cheltuiala, get_str, get_nr_ap, get_suma, get_data, get_tipul, get_id
from Logic.Adunare_val_pt_data import adunare_valoare_for_data
from Logic.Afis_sume_lunare import get_sume_lunare
from Logic.Biggest_cheltuiala_pt_tip import find_out_biggest_cheltuiala_for_tip
from Logic.Ordonare_desc import ordonare
from Logic.Stergere_cheltuieli import sterge_pt_nr_ap
from Logic.crud import adaugare, read, modif, stergere


def show_menu():
    print('1.CRUD')
    print('2.Stergerea tuturor cheltuielilor pentru un apartament dat')
    print('3.Adunarea unei valori la toate cheltuielile dintr-o dată citită.')
    print('4.Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.')
    print('5.Ordonarea cheltuielilor descrescător după sumă.')
    print('6.Afișarea sumelor lunare pentru fiecare apartament.')
    print('x.Oprire')


def handle_add(lst_cheltuieli):
    try:
        id_ap = int(input('Introduceti id-ul cheltuielii aici: '))#nu are rost sa faci functie de test, id ul DEJA trebuie introdus de tip int
        nr_ap = int(input('Introduceti numarul apartamentului aici: '))
        suma = int(input('Introduceti suma cheltuielii aici: '))
        data = input('Introduceti data in care s - a emis cheltuiala in format DD.MM.YYYY aici: ')
        tip = input('Introduceti tipul cheltuielii aici: ')
        new_cheltuiala = creeaza_cheltuiala(id_ap, nr_ap, suma, data, tip)
        lst_cheltuieli = adaugare(lst_cheltuieli,id_ap, nr_ap, suma, data, tip)
    except ValueError as ve:
        print('Eroare:', ve)
    return lst_cheltuieli

def handle_show_all(lst_cheltuieli):
    for cheltuiala in lst_cheltuieli:
        print(get_str(cheltuiala))


def handle_show_details(lst_cheltuieli):
    try:
        id_ap = int(input('Introduceti aici Numarul cheltuielii despre care vrem sa aflam detalii: '))
        cheltuiala = read(lst_cheltuieli, id_ap)
        if cheltuiala == None:
            print('Nu ati introdus un id existent, deci consideram prima cheltuiala!')
            cheltuiala = lst_cheltuieli[0]
        print(f'Id-ul cheltuielii:{get_id(cheltuiala)}')
        print(f'Nr_apartament:{get_nr_ap(cheltuiala)}')
        print(f'Suma:{get_suma(cheltuiala)}')
        print(f'Data:{get_data(cheltuiala)}')
        print(f'Tip:{get_tipul(cheltuiala)}')
    except ValueError as ve:
        print('Eroare: ', ve)

def handle_modif(lst_cheltuieli):
    try:
        id_ap = int(input('Introduceti id-ul cheltuielii care doriti sa se modifice: '))
        nr_ap = int(input('Dati numarul apartamentului al cheltuielii care se actualizeaza: '))
        suma = int(input('Dati aici noua suma a cheltuielii: '))
        data = input('Dati aici noua data a cheltuielii: ')
        tip = input('Dati aici noul tip al cheltuielii: ')
        new_cheltuiala = creeaza_cheltuiala(id_ap, nr_ap, suma, data, tip)
        lst_cheltuieli = modif(lst_cheltuieli, new_cheltuiala)
    except ValueError as ve:
        print('Eroare:', ve)
    return lst_cheltuieli


def handle_delete(lst_cheltuieli):
    try:
        id = int(input('Dati aici id-ul cheltuielii care doriti sa se stearga: '))
        lst_cheltuieli = stergere(lst_cheltuieli, id)
    except ValueError as ve:
        print('Eroare:', ve)
    else:
        print("S-a sters cu succes cheltuiala!")
    return lst_cheltuieli

def handle_crud(lst_cheltuieli):
    while True:
        print('1.Creeaza')
        print('2.Modifica')
        print('3.Sterge')
        print('a.Afiseaza_cheltuieli')
        print('d.Afiseaza_detalii_cheltuiela')
        print('b.Revenire')
        optiune = input('Introduceti optiunea dorita aici: ')
        if optiune == '1':
            lst_cheltuieli = handle_add(lst_cheltuieli)
        elif optiune == '2':
            lst_cheltuieli = handle_modif(lst_cheltuieli)
        elif optiune == '3':
            lst_cheltuieli = handle_delete(lst_cheltuieli)
        elif optiune == 'a':
            handle_show_all(lst_cheltuieli)
        elif optiune == 'd':
            handle_show_details(lst_cheltuieli)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')
    return lst_cheltuieli


def handle_delete_for_nr_ap(lst_cheltuieli):
    try:
        nr_ap = int(input('Introduceti numarul apartamentului aici: '))
        lst_cheltuieli = sterge_pt_nr_ap(lst_cheltuieli, nr_ap)
    except ValueError as ve:
        print('Eroare:', ve)
    else:
        print(f'S-au sters cu succes cheltuielile ce aveau numarul apartamentului {nr_ap}')
    return lst_cheltuieli


def handle_add_for_data(lst_cheltuieli):
    try:
        data = input('Introduceti o data aici pentru care cautam cheltuieli aici: ')
        val = int(input('Introduceti valoarea cu care se modifica cheltuielile aici: '))
        lst_cheltuieli = adunare_valoare_for_data(lst_cheltuieli, data, val)
    except ValueError as ve:
        print('Eroare:', ve)
    else:
        print('Valorile s au adaugat cu succes!')
    return lst_cheltuieli


def handle_show_biggest_sum_for_each_type(lst_cheltuieli):
    result = find_out_biggest_cheltuiala_for_tip(lst_cheltuieli)
    for tip in result:
        print(f'Pentru tipul: {tip} avem cheltuiala: {get_str(result[tip])}')


def handle_sort_reverse(lst_cheltuieli):
    lst_cheltuieli = ordonare(lst_cheltuieli)
    print('Ordonarea s a facut cu succes! ')
    return lst_cheltuieli


def handle_show_sums_for_each_month(lst_cheltuieli):
    result = get_sume_lunare(lst_cheltuieli)
    for luna in result:
        print(f'Pentru Luna {luna} avem lista de sume: {result[luna]}')


def run_ui(lst_cheltuieli):
    while True:
        show_menu()
        optiune = input('Introduceti optiunea dorita aici: ')
        if optiune == '1':
            lst_cheltuieli = handle_crud(lst_cheltuieli)
        elif optiune == '2':
            lst_cheltuieli = handle_delete_for_nr_ap(lst_cheltuieli)
        elif optiune == '3':
            lst_cheltuieli = handle_add_for_data(lst_cheltuieli)
        elif optiune == '4':
            handle_show_biggest_sum_for_each_type(lst_cheltuieli)
        elif optiune == '5':
            lst_cheltuieli = handle_sort_reverse(lst_cheltuieli)
            handle_show_all(lst_cheltuieli)
        elif optiune == '6':
            handle_show_sums_for_each_month(lst_cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')
    return lst_cheltuieli