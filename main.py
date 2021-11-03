from Logic.crud import adaugare
from Tests.Test_Adunare_val_pt_data import test_adunare_valoare_pt_data
from Tests.Test_Afis_sume_lunare import test_get_sume_lunare
from Tests.Test_Crud import test_adaugare, test_crud
from Tests.Test_Ordonare_desc import test_ordonare
from Tests.Test_Stergere_cheltuilei import test_Stergere_cheltuieli
from Tests.Test_find_out_biggest_cheltuiala_for_tip import test_find_out_biggest_cheltuiala_for_tip
from User_Interface.console import run_ui


def main():
    lst_cheltuieli = []
    tip_cheltuiala = ['intreținere', 'canal', 'alte cheltuieli']
    lst_cheltuieli = adaugare(lst_cheltuieli, 1, 3, 234.5, '28.11.2004', 'alte cheltuieli')
    lst_cheltuieli = adaugare(lst_cheltuieli, 2, 1, 300, '27.11.2004', 'canal')
    lst_cheltuieli = adaugare(lst_cheltuieli, 3, 2, 234.5, '27.11.2004', 'intretinere')
    lst_cheltuieli = adaugare(lst_cheltuieli, 4, 4, 400, '27.11.2004', 'intretinere')
    lst_cheltuieli = adaugare(lst_cheltuieli, 5, 1, 560, '27.11.2004', 'canal')
    lst_cheltuieli = adaugare(lst_cheltuieli, 6, 5, 700, '30.08.2004', 'canal')
    lst_cheltuieli = run_ui(lst_cheltuieli)#lista de cheltuilei ce se obtine in urma apelatii aplicatiei


if __name__ == '__main__':
    test_crud()
    test_Stergere_cheltuieli()
    test_adunare_valoare_pt_data()
    test_find_out_biggest_cheltuiala_for_tip()
    test_ordonare()
    test_get_sume_lunare()
    main()