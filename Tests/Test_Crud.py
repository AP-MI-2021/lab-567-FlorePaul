from Domain.cheltuieli import creeaza_cheltuiala, get_nr_ap, get_id
from Logic.crud import adaugare, stergere, modif
from Logic.crud import read

def get_data():
    return [
        creeaza_cheltuiala(1, 1, 250, '12.10.2002', 'intretinere'),#Primul e ID-ul, al DOILEA e Numarul Apartamentului!
        creeaza_cheltuiala(2, 2, 100, '12.10.2012', 'intretinere'),
        creeaza_cheltuiala(3, 3, 175, '10.10.2002', 'alte cheltuieli'),
        creeaza_cheltuiala(4, 4, 323.0, '07.07.2020', 'canal'),
        creeaza_cheltuiala(5, 5, 123.3, '08.12.2010', 'alte cheltuieli')
        ]

def test_adaugare():
    lst_cheltuieli = get_data()
    cheltuiala_nou = (6, 6, 222, '12.10.2002', 'canal')
    new_cheltuiala = creeaza_cheltuiala(*cheltuiala_nou)
    new_lst_cheltuieli = adaugare(lst_cheltuieli, *cheltuiala_nou)
    assert len(new_lst_cheltuieli) == len(lst_cheltuieli) + 1

    gasit = False
    for cheltuiala in lst_cheltuieli:
        if cheltuiala == new_cheltuiala:
            gasit = True
    assert gasit == False # nu apare in lista veche, e ok

    gasit = False
    for cheltuiala in new_lst_cheltuieli:
        if cheltuiala == new_cheltuiala:
            gasit = True
    assert  gasit == True

def test_read():
    lst_cheltuieli = get_data()
    nr_apartament = lst_cheltuieli[2] # sau direct nr_apartament = 3, a 3 a cheltuiala din lista(care, evident, se afla in lista)
    caut_cheltuiala = read(lst_cheltuieli, get_id(nr_apartament))
    assert caut_cheltuiala in lst_cheltuieli
    assert read(lst_cheltuieli, None) == lst_cheltuieli

def test_modif():
    lst_cheltuieli = get_data()
    schimbat_cheltuiala = (3, 3, 375, '12.10.2002', 'intretinere')
    new_cheltuiala = creeaza_cheltuiala(*schimbat_cheltuiala)
    new_lst_cheltuieli = modif(lst_cheltuieli, new_cheltuiala)
    assert len(new_lst_cheltuieli) == len(lst_cheltuieli)#evident, am modificat o cheltuiala, deci au aceeasi lungime
    assert new_cheltuiala not in lst_cheltuieli
    assert new_cheltuiala in new_lst_cheltuieli

def test_stergere():
    lst_cheltuieli = get_data()
    id_ap = 3
    new_lst_cheltuiala = stergere(lst_cheltuieli, id_ap)
    assert len(new_lst_cheltuiala) == len(lst_cheltuieli)- 1
    aparitie_cheltuiala = read(lst_cheltuieli, id_ap)
    assert aparitie_cheltuiala not in new_lst_cheltuiala
    assert aparitie_cheltuiala in lst_cheltuieli

def test_crud():
    test_modif()
    test_read()
    test_adaugare()
    test_stergere()




