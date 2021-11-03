from Domain.cheltuieli import get_suma, creeaza_cheltuiala, get_str
from Logic.Biggest_cheltuiala_pt_tip import find_out_biggest_cheltuiala_for_tip
from Tests.Test_Crud import get_info


def test_find_out_biggest_cheltuiala_for_tip():
    lista_cheltuieli = get_info()
    result = find_out_biggest_cheltuiala_for_tip(lista_cheltuieli)
    assert len(result) == 3
    assert get_suma(result['alte cheltuieli']) == 275
    assert get_suma(result['intretinere']) > 100
    cheltuiala = creeaza_cheltuiala(4, 4, 323.0, '07.07.2020', 'canal')
    assert get_str(result['canal']) == get_str(cheltuiala)
