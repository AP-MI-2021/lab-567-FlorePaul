from Domain.cheltuieli import get_data, creeaza_cheltuiala, get_id, get_nr_ap, get_tipul, get_suma
from Logic.crud import format_data


def adunare_valoare_for_data(lst_cheltuieli, data: str, val: int):
    '''
    Functia aduna la suma fiecarei cheltuieli ce au o anumita data o valoare
    :param lst_cheltuieli:O lista de cheltuieli
    :param data:O data introdusa de utilizator
    :param val:O valoare introdusa de utilizator
    :return:Returneaza lista obtinuta in urma schimbarii preturilor pentru cheltuielile corespunzatoare
    '''
    format_data(data)   #Verificam daca data introdusa de utilizator este corecta
    new_lst_cheltuieli = []
    minim_o_cheltuiala = False
    for cheltuiala in lst_cheltuieli:
        if get_data(cheltuiala) == data:    #o cheltuiala "corespunzatoare"
            minim_o_cheltuiala = True
            suma_noua = get_suma(cheltuiala) + val  #suma noua
            id = get_id(cheltuiala)
            nr_ap = get_nr_ap(cheltuiala)
            tip = get_tipul(cheltuiala)
            new_lst_cheltuieli.append(creeaza_cheltuiala(id, nr_ap, suma_noua, data, tip))
        else:
            new_lst_cheltuieli.append(cheltuiala)
    if minim_o_cheltuiala == False: #nu am facut nici o modificare
        raise ValueError(f'Nu exista nici o cheltuiala cu data {data} !')
    return new_lst_cheltuieli