from Domain.Vanzare import creeaza_carte, get_sale, get_price
from Logic.modify_prices import modify_prices


def get_data():
    return [
        creeaza_carte(1, 'b1','g1', 30.0, 'None'),
        creeaza_carte(2, 'b2', 'g2', 23.89, 'Silver'),
        creeaza_carte(3,'b3','g3',29,'None'),
        creeaza_carte(4,'b4','g4',30,'Gold'),
        creeaza_carte(5,'b5','g5',100.50,'Gold'),
        creeaza_carte(6,'b6','g6',10,'None'),



    ]


def test_modify_prices():
    vanzari = get_data()
    undo_list = []
    redo_list = []
    new_list = modify_prices(vanzari, [], [])
    assert len(vanzari) == len(new_list)
    for vanzare in new_list:
        assert get_sale(vanzare) == 'None'
    index = 0
    while index < len(vanzari):
        if get_sale(vanzari[index]) is not 'None':
            assert get_price(new_list[index]) != get_price(vanzari[index])
        index += 1
