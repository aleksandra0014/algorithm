
from linear_search import create_list


def binary_search(arr, low, high, x, param):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid][param] > x[param]:
            return binary_search(arr, low, mid - 1, x, param)

        else:
            return binary_search(arr, mid + 1, high, x, param)

    else:
        return 'Brak'


if __name__ == '__main__':
    tab = create_list('plik_roboty2.csv')
    param = int(input('Wpisz parameter: (typ=0, cena=1, zasieg=2, kamera=3): '))
    sorted_tab = sorted(tab, key=lambda x: x[param])
    print(sorted_tab)

    lista_par1 = ['AGV', 1213, 8, 1]
    print(f'Znajdź robota: {lista_par1}')
    find1 = binary_search(sorted_tab, 0, len(sorted_tab) - 1, lista_par1, param)
    if isinstance(find1, int):
        print(sorted_tab[find1])
    else:
        print(find1)

    lista_par2 = ['ASV', 10.0, 8, 0]
    print(f'Znajdź robota: {lista_par2}')
    find2 = binary_search(sorted_tab, 0, len(sorted_tab)-1, lista_par2, param)
    if isinstance(find2, int):
        print(sorted_tab[find2])
    else:
        print(find2)

