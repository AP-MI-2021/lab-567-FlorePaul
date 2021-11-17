from Logic.crud import adaugare
from Tests.Test_Adunare_val_pt_data import test_adunare_valoare_pt_data
from Tests.Test_Afis_sume_lunare import test_get_sume_lunare
from Tests.Test_Crud import test_adaugare, test_crud
from Tests.Test_Ordonare_desc import test_ordonare
from Tests.Test_Stergere_cheltuilei import test_Stergere_cheltuieli
from Tests.Test_Undo_and_Redo import test_undo_and_redo, Teste_For_All_Undo_And_Redo
from Tests.Test_find_out_biggest_cheltuiala_for_tip import test_find_out_biggest_cheltuiala_for_tip
from User_Interface.command_line_console import run_in_line_console
from User_Interface.console import run_ui

def meniuri():
    print('1.Meniul vechi')
    print('2.Meniul nou')
    print('x.Exit')

def main():
    lst_cheltuieli = []
    tip_cheltuiala = ['intreținere', 'canal', 'alte cheltuieli']
    undo_list = []
    redo_list = []
    lst_cheltuieli = adaugare(lst_cheltuieli, 1, 3, 234.5, '28.11.2004', 'alte cheltuieli', undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 2, 1, 300, '27.11.2004', 'canal', undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 3, 2, 234.5, '27.11.2004', 'intretinere', undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 4, 4, 400, '27.11.2004', 'intretinere', undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 5, 1, 560, '27.11.2004', 'canal', undo_list, redo_list)
    lst_cheltuieli = adaugare(lst_cheltuieli, 6, 5, 700, '30.08.2004', 'canal', undo_list, redo_list)
    while True:
        meniuri()
        optiune = input('Alegeti interfata: ')
        if optiune == '1':
            run_ui(lst_cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            run_in_line_console(lst_cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')


if __name__ == '__main__':
    test_crud()
    test_Stergere_cheltuieli()
    test_adunare_valoare_pt_data()
    test_find_out_biggest_cheltuiala_for_tip()
    test_ordonare()
    Teste_For_All_Undo_And_Redo()
    main()