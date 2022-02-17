from Logic.general_logic import create
from Tests.test_crud import test_crud
from Tests.test_modify_prices import test_modify_prices
from Tests.test_undo_redo import test_undo_redo
from UserInterface.console import run_ui


def main():
    undo_list = []
    redo_list = []
    vanzari = []
    vanzari = create(vanzari, 1, 'Spider-Man', 'Sci-Fi', 60, 'Silver', undo_list, redo_list)
    vanzari = create(vanzari, 2, 'Marvel: Adventures', 'Sci-Fi', 50, 'Gold', undo_list, redo_list)
    vanzari = create(vanzari, 3, 'Man in Black', 'Fiction', 25.50, 'None', undo_list, redo_list)
    vanzari = create(vanzari, 4, 'Return Home', 'Comic', 15.76, 'Silver', undo_list, redo_list)

    vanzari = run_ui(vanzari, undo_list, redo_list)


if __name__ == '__main__':
    test_crud()
    test_modify_prices()
    test_undo_redo()
    main()