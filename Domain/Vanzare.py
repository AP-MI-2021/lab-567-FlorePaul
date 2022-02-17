def creeaza_carte(id_vanzare: int, titlu_carte: str, gen_carte: str, pret: float, reducere_client: str):
    """
    Creeaza o vanzare.
    :param id_carte:id-ul vanzarii
    :param titlu_carte: titlul cartii ce urmeaza a fi introdusa spre vanzare
    :param gen_carte: genul cartii ce urmeaza a fi introdusa spre vanzare
    :param pret: pretul cartii
    :param reducere_client: tipul cardului de fidelitate
    :return: o vanzare
    """
    """
     return{'id': id_vanzare,
           'titlu': titlu_carte,
           'gen': gen_carte,
           'pret': pret,
           'reducere': reducere_client}
    """
    return [id_vanzare, titlu_carte, gen_carte, pret, reducere_client]


def get_id(vanzare):
    """
    Getter pentru id-ul vanzarii
    :param vanzare: vanzarea
    :return: id-ul vanzarii
    """
    return vanzare[0]


def get_title(vanzare):
    """
    Getter pentru titlul cartii
    :param vanzare: vanzarea
    :return: titlul cartii din vanzare
    """
    return vanzare[1]


def get_genre(vanzare):
    """
    Getter pentru genul cartii
    :param vanzare: vanzarea
    :return: genul cartii din vanzare
    """
    return vanzare[2]


def get_price(vanzare):
    """
    Getter pentru pretul cartii
    :param vanzare: vanzarea
    :return: pretul cartii din vanzare
    """
    return vanzare[3]


def get_sale(vanzare):
    """
    Getter pentru tipul reducerii aplicate fiecarui client
    :param vanzare: vanzarea
    :return: tipul reducerii clientului
    """
    return vanzare[4]


def get_string(vanzare):
    return f'Vanzarea cu id-ul {get_id(vanzare)} contine cartea {get_title(vanzare)}'