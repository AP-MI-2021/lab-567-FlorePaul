from Domain.Vanzare import creeaza_carte, get_id
from Logic.general_logic import create, read, delete, update


def get_data():
    return [
        creeaza_carte(1, 'b1','g1', 30.0, 'None'),
        creeaza_carte(2, 'b2', 'g2', 23.89, 'Silver'),
        creeaza_carte(3,'b3','g3',29,'None'),
        creeaza_carte(4,'b4','g4',30,'Gold'),
        creeaza_carte(5,'b5','g5',100.50,'Gold'),
        creeaza_carte(6,'b6','g6',10,'None'),



    ]


def test_create():
    vanzari = get_data()
    params = (20, 'bnew', 'gnew', 1600, 'Silver', [], [])
    s_new = creeaza_carte(*params[:-2])
    new_vanzari = create(vanzari, *params)
    assert len(new_vanzari) == len(vanzari) + 1
    assert s_new in new_vanzari
    params2 = (20, 'New', 'New', 200, 'None', [], [])
    try:
        _ = create(new_vanzari, *params2)
        assert False
    except ValueError:
        assert True


def test_read():
    vanzari = get_data()
    some_s = vanzari[4]
    assert read(vanzari, get_id(some_s)) == some_s
    assert read(vanzari, None) == vanzari


def test_update():
    vanzari = get_data()
    s_updated = creeaza_carte(1, 'new name', 'new genre', 198.87, 'None')
    updated = update(vanzari, s_updated, [], [])
    assert s_updated in updated
    assert s_updated not in vanzari
    assert len(updated) == len(vanzari)


def test_delete():
    vanzari = get_data()
    to_delete = 3
    s_deleted = read(vanzari, to_delete)
    deleted = delete(vanzari, to_delete, [], [])
    assert s_deleted not in deleted
    assert s_deleted in vanzari
    assert len(deleted) == len(vanzari) - 1


def test_crud():
    test_create()
    #test_read()
    test_update()
    test_delete()

