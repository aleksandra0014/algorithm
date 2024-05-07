import pandas as pd

def create_list(file_path):
    df = pd.read_csv(file_path, header=None)
    tab = df.to_numpy().tolist()
    return tab

def linear_search(arr, value):
    # sprawdzanie typu
    typ, cena, zasieg, kamera  = False, False, False, False
    find = []

    for i in range(len(arr)):

        # typ
        if value[0] is None:
            typ = True
        elif isinstance(value[0], list):
            if arr[i][0] in value[0]:
                typ = True
        else:
            if arr[i][0] == value[0]:
                typ = True

        # cena
        if value[1] is None:
            cena = True
        elif isinstance(value[1], list):
            if arr[i][1] in value[1]:
                cena = True
        else:
            if arr[i][0] == value[1]:
                cena = True

        # zasieg
        if value[2] is None:
            zasieg = True
        elif isinstance(value[2], list):
            if arr[i][2] in value[2]:
                zasieg = True
        else:
            if arr[i][0] == value[2]:
                zasieg = True

        # kamera
        if value[3] is None:
            kamera = True
        elif isinstance(value[3], list):
            if arr[i][3] in value[3]:
                kamera = True
        else:
            if arr[i][3] == value[3]:
                kamera = True

        if typ and cena and zasieg and kamera:
            find.append(arr[i])

        typ, cena, zasieg, kamera = False, False, False, False

    if len(find) == 0:
        return 'Brak'
    else:
        return find



if __name__ == '__main__':
    tab = create_list('plik_roboty2.csv')
    print(tab)
    lista_par1 = ['AGV', None, [5, 6, 7, 8, 9, 10], 1]
    print(f'Znajdź robota: {lista_par1}')
    find = linear_search(tab, lista_par1)
    print(find)
    lista_par2 = ['ASV', None, [5, 6, 7, 8, 9, 10], 0]
    print(f'Znajdź robota: {lista_par2}')
    find2 = linear_search(tab, lista_par2)
    print(find2)
