from Domain.Vanzare import get_title, creeaza_carte, get_sale, get_price, get_genre, get_id
from Logic.general_logic import update


def modify_g(vanzari, to_modify, genre):
    """
    Modifica genul cartii dintr-o vanzare, pe baza numelui acesteia
    :param vanzari: lista de vanzari
    :param to_modify: numele cartii care necesita modificari
    :param genre: noul gen al cartii
    :return: lista modificata
    """
    for vanzare in vanzari:
        nume = get_title(vanzare)
        if nume == to_modify:
            id = get_id(vanzare)
            price = get_price(vanzare)
            reducere = get_sale(vanzare)
            vanzari = update(vanzari, creeaza_carte(id, nume, genre, price, reducere))
        else:
            raise ValueError('Cartea cu numele introdus nu exista in baza de date')
    return vanzari