from Domain.Vanzare import get_sale, get_id, get_title, get_genre, get_price, creeaza_carte
from Logic.general_logic import update


def apply_discount_silver(price):
    """
   Calculeaza pretul dupa o reducere de 5%
   :param price: pretul initial
   :return: pretul redus
   """
    discount = 5 * price / 100
    return price - discount


def apply_discount_gold(price):
    """
   Calculeaza pretul dupa o reducere de 10%
   :param price: pretul initial
   :return: pretul redus
   """
    discount = 10 * price / 100
    return price - discount


def modify_prices(lst_vanzari, undo_list, redo_list):
   """
  Modifica pretul vanzarilor in functie de tipul de reducere aplicat fiecareia
   :param redo_list:
   :param undo_list:
  :param lst_vanzari: lista de vanzari
  :return: lst_vanzari dupa aplicarea discount-urilor
  """

   for vanzare in lst_vanzari:
      reducere = get_sale(vanzare)
      id = get_id(vanzare)
      nume = get_title(vanzare)
      gen = get_genre(vanzare)
      price = get_price(vanzare)
      if reducere == 'Silver':
         lst_vanzari = update(lst_vanzari,creeaza_carte(id, nume, gen, apply_discount_silver(price), 'None'), undo_list, redo_list)
      elif reducere == 'Gold':
         lst_vanzari = update(lst_vanzari, creeaza_carte(id, nume, gen, apply_discount_gold(price), 'None'), undo_list, redo_list)
      elif reducere == 'None':
          pass
      else:
         raise TypeError('Reducerea nu este introdusa corect')
   return lst_vanzari
