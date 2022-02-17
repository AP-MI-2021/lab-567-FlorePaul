from Domain.Vanzare import get_id
from Logic.general_logic import create
from Logic.undo_redo import do_undo, do_redo
from UserInterface.console import handle_undo


def test_undo_redo():
    vanzari = []
    undo_list = []
    redo_list = []
    vanzari = create(vanzari, 1, 'o1', 'g1', 20, 'Silver', undo_list, redo_list)
    vanzari = create(vanzari, 2, 'o2', 'g2', 30, 'None', undo_list, redo_list)
    vanzari = create(vanzari, 3, 'o3', 'g3', 50, 'Gold', undo_list, redo_list)
    # after 3 add commands
    assert len(vanzari) == 3

    vanzari = do_undo(undo_list, redo_list, vanzari)
    # first undo

    assert len(vanzari) == 2
    assert len(redo_list) == 1
    assert len(undo_list) == 2

    vanzari = do_undo(undo_list, redo_list, vanzari)
    # second undo

    assert len(vanzari) == 1
    assert len(redo_list) == 2
    assert len(undo_list) == 1

    vanzari = do_undo(undo_list, redo_list, vanzari)
    # third undo

    assert len(vanzari) == 0
    assert len(redo_list) == 3
    assert len(undo_list) == 0

    vanzari = do_undo(undo_list, redo_list, vanzari)
    # fourth undo - nothing happens

    assert len(vanzari) == 0
    assert len(redo_list) == 3
    assert len(undo_list) == 0

    vanzari = do_undo(undo_list, redo_list, vanzari)
    # fifth undo - also nothing happens

    assert len(vanzari) == 0
    assert len(redo_list) == 3
    assert len(undo_list) == 0

    vanzari = create(vanzari, 1, 'o1', 'g1', 20, 'Silver', undo_list, redo_list)
    vanzari = create(vanzari, 2, 'o2', 'g2', 30, 'None', undo_list, redo_list)
    vanzari = create(vanzari, 3, 'o3', 'g3', 50, 'Gold', undo_list, redo_list)

    # 3 more add commands
    assert len(vanzari) == 3

    redo_list = do_redo(undo_list, redo_list, vanzari)
    #first redo

    assert len(vanzari) == 3
    assert len(redo_list) == 0
    assert len(undo_list) == 3

    vanzari = do_undo(undo_list, redo_list, vanzari)
    vanzari = do_undo(undo_list, redo_list, vanzari)
    # 2 undos

    assert len(vanzari) == 1
    assert len(redo_list) == 2
    assert len(undo_list) == 1

    vanzari = do_redo(undo_list, redo_list, vanzari)
    # second redo

    assert len(vanzari) == 2
    assert len(undo_list) == 2
    assert len(redo_list) == 1

    vanzari = do_redo(undo_list, redo_list, vanzari)
    # third redo

    assert len(vanzari) == 3
    assert len(undo_list) == 3
    assert len(redo_list) == 0

    vanzari = do_undo(undo_list, redo_list, vanzari)
    vanzari = do_undo(undo_list, redo_list, vanzari)
    # 2 undos

    assert len(vanzari) == 1
    assert len(redo_list) == 2
    assert len(undo_list) == 1

    vanzari = create(vanzari, 4, 'o4', 'g4', 20, 'None', undo_list, redo_list)
    #add o4

    assert len(vanzari) == 2
    assert get_id(vanzari[1]) == 4

    redo_list = do_redo(undo_list, redo_list, vanzari)
    # one more redo

    assert len(vanzari) == 2
    assert get_id(vanzari[1]) == 4

    vanzari = do_undo(undo_list, redo_list, vanzari)
    # one more undo
    assert len(vanzari) == 1
    assert len(undo_list) == 1
    assert len(redo_list) == 1

    vanzari = do_undo(undo_list, redo_list, vanzari)
    #  undo

    assert len(vanzari) == 0
    assert len(undo_list) == 0
    assert len(redo_list) == 2

    vanzari = do_redo(undo_list, redo_list, vanzari)
    vanzari = do_redo(undo_list, redo_list, vanzari)
    # after 2 redo s

    assert len(vanzari) == 2
    assert len(undo_list) == 2
    assert len(redo_list) == 0

    redo_list = do_redo(undo_list, redo_list, vanzari)
    # last redo

    assert len(vanzari) == 2
    assert len(undo_list) == 2
    assert len(redo_list) == 0





