from Domain.Vanzare import creeaza_carte, get_id, get_sale, get_title, get_genre, get_price


def id_list(lst_vanzari):
    list = []
    for num in range(0, len(lst_vanzari)):
        list.append(get_id(lst_vanzari[num]))
    return list


def create(lst_vanzari,
           id_vanzare: int, titlu_carte: str, gen_carte: str, pret: float, reducere_client: str, undo_list: list, redo_list: list):
    """

   :param lst_vanzari: lista de vanzari.
   :param id_vanzare: id-ul vanzarii
   :param titlu_carte: titlul cartii din vanzarea curenta
   :param gen_carte: genul cartii
   :param pret: pretul cartii
   :param reducere_client: tipul reducerii
   :param undo_list:
   :param redo_list:
   :return: o lista formata din lst_vanzari si o noua vanzare adaugata
   """
    s_list = ["None", "Gold", "Silver"]
    if id_vanzare in id_list(lst_vanzari):
        raise ValueError('Id-ul introdus exista deja!')
    if reducere_client not in s_list:
        raise TypeError('Tip reducere nerecunoscut')

    vanzare = creeaza_carte(id_vanzare, titlu_carte, gen_carte, pret, reducere_client)
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return lst_vanzari + [vanzare]


def read(lst_vanzari, id_vanzare = None):

    """
    Citeste o vanzare
    :param lst_vanzari:
   :param lst_vanzari:lista de vanzari
   :param id_vanzare: id-ul vanzarii
   :return: vanzarea cu id-ul id_vanzare sau lista cu vanzari daca id_vanzare = None
    """
    check_vanzare = None
    for vanzari in lst_vanzari:
        if get_id(vanzari) == id_vanzare:
            check_vanzare = vanzari
    if check_vanzare:
        return check_vanzare
    return None

def update(lst_vanzari, new_vanzare, undo_list, redo_list):
    """
    Actualizeaza o vanzare existenta
    :param redo_list: lista de redo
    :param undo_list: lista de undo
    :param lst_vanzari: lista de vanzari
    :param new_vanzare: vanzarea cu care se va inlocui cea existenta deja pe acel id-ul
    :return: o lista ce contine vanzarea actualizata
    """
    if read(lst_vanzari, get_id(new_vanzare)) is None:
        raise ValueError(f'Nu xista o vanzare cu id-ul {get_id(new_vanzare)} pe care sa o modificam.')

    new_list = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != get_id(new_vanzare):
            new_list.append(vanzare)
        else:
            new_list.append(new_vanzare)

    undo_list.append(lst_vanzari)
    redo_list.clear()

    return new_list


def delete(lst_vanzari, id_vanzare: int, undo_list, redo_list):
    """
   Sterge o vanzare existenta din lista
   :param lst_vanzari: lista de vanzari
   :param id_vanzare: id-ul vanzarii care urmeaza a fi stearsa
   :return: lista cu vanzari fara vanzarea cu id-ul id_vanzare
   """
    if read(lst_vanzari, id_vanzare) is None:
        raise ValueError(f'Nu exista o vanzare cu id-ul {id_vanzare} pe care sa o stergem')
    new_list = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_list.append(vanzare)
    if len(new_list) == len(lst_vanzari):
        raise ValueError('Id-ul introdus nu exista!')
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return new_list
