from Domain.Vanzare import get_genre, get_title


def show_distinct_number(vanzari):
    """
    Numara cate titluri distincte se afla in fiecare gen.
    :param vanzari: Lista de vanzari
    :return: Dictionar de tipul (gen, numar de titluri distincte)
    """
    result = {}
    titles = []
    for vanzare in vanzari:
        gen = get_genre(vanzare)
        title = get_title(vanzare)
        if gen in result:
            if title not in titles:
                titles.append(title)
                result[gen] += 1
            else:
                pass
        else:
            titles.append(title)
            result[gen] = 1

    return result