from Logic.crud import adaugare
from Tests.Test_Crud import test_adaugare, test_crud
from User_Interface.console import run_ui


def main():
    lst_cheltuieli = []
    tip_cheltuiala = ['intreținere', 'canal', 'alte cheltuieli']
    lst_cheltuieli = adaugare(lst_cheltuieli, 1, 1, 234.5, '27.11.2004', 'canal')
    lst_cheltuieli = adaugare(lst_cheltuieli, 2, 1, 300, '27.11.2004', 'canal')
    lst_cheltuieli = adaugare(lst_cheltuieli, 3, 2, 234.5, '27.11.2004', 'canal')
    lst_cheltuieli = adaugare(lst_cheltuieli, 4, 1, 400, '27.11.2004', 'canal')
    lst_cheltuieli = adaugare(lst_cheltuieli, 5, 1, 560, '27.11.2004', 'canal')
    lst_cheltuieli = adaugare(lst_cheltuieli, 6, 1, 700, '27.11.2004', 'canal')
    lst_cheltuieli = run_ui(lst_cheltuieli)#lista de cheltuilei ce se obtine in urma apelatii aplicatiei

if __name__ == '__main__':
    test_crud()
    main()