from Domain.cheltuieli import creeaza_cheltuiala, get_nr_ap, get_id


def adaugare(lst_cheltuieli, id, nr_ap, suma, data, tip):
    '''
    Subprogramul adauga in lista "cheltuieli" noua cheltuiele cu datele introduse de utilizator
    :param lst_cheltuieli: O lista de cheltuieli
    :param id: Id ul cheltuielii
    :param nr_ap: Nr. apartamentului noii cheltuieli
    :param suma: Suma noii cheltuieli
    :param data: Data noii cheltuieli
    :param tip: Tipul acesteia
    :return: O lista noua, obtinuta prin adaugarea noii cheltuielo
    '''
    new_cheltuiala = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
    return lst_cheltuieli + [new_cheltuiala]

def stergere(lst_cheltuieli, id):
    '''
    Sterge din lista cheltuiala cu un id al cheltuielii dat
    :param lst_cheltuieli: O lista de cheltuieli
    :param id: Id ul unei cheltuieli dat
    :return: Lista obtinuta prin eliminarea cheltuielii anume
    '''
    result_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id:
            result_cheltuieli.append(cheltuiala)
    return result_cheltuieli

def modif(lst_cheltuiali, new_cheltuiala):
    '''
    Functia modifica (inlocuieste) cheltuiala pentru un anumit id de nr de aprtament cu o alta
    :param lst_cheltuiali: O lista de cheltuieli
    :param new_cheltuiala: Noua cheltuiala pentru un numar de apartament stiut
    :return: Lista noua obtinuta prin inlocuire
    '''
    new_lst_cheltuiala = []
    for cheltuiala in lst_cheltuiali:
        if get_id(cheltuiala) != get_id(new_cheltuiala):
            new_lst_cheltuiala.append(cheltuiala)
        else:
            new_lst_cheltuiala.append(new_cheltuiala)
    return new_lst_cheltuiala

def read(lst_cheltuieli, id_ap_cheltuiala = None):
    '''
    Functia verifica daca apare in lista de cheltuieli o anumita cheltuiala, cu id dat
    :param lst_cheltuieli:O lista de cheltueieli
    :param id_ap_cheltuiala:Numarul apartamentului a cheltuielii
    :return:Returneaza cheltuiala cautata (daca exista in lista) sau toata lista daca nr_ap_cheltuiala = None
    '''
    cheltuiala_cu_nr_ap = None
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == id_ap_cheltuiala: #am gasit cheltuiala
            cheltuiala_cu_nr_ap = cheltuiala
    if cheltuiala_cu_nr_ap:
        return cheltuiala_cu_nr_ap
    return lst_cheltuieli#nu am gasit cheltuiala