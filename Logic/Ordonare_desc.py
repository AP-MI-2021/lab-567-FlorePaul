from Domain.cheltuieli import get_suma


def ordonare(lista):
     '''
     Functia returneaza o lista de cheltuieli ordonate descrescator in functie de sumele acestora
     :param lista: O lista de cheltuieli
     :return: Lista ordonata descrescator, "cheia" find sumelele cheltuielilor
     '''
     return sorted(lista, key = get_suma, reverse  = True)
