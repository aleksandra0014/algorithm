from collections import Counter
import time
from matplotlib import pyplot as plt


def rozklad(n):
    p = 2
    D = []
    while n > 1:
        if n % p == 0:
            n = n/p
            D.append(p)
        else:
            p += 1
    return D

def RNWD(a,b):
    da = rozklad(a)
    db = rozklad(b)
    c1 = Counter(da)
    c2 = Counter(db)
    czesc_wspolna = list((c1 & c2).elements())

    nwd = 1
    for el in czesc_wspolna:
        nwd *= el

    return nwd

def ENWD(a, b):
    if b:
        return ENWD(b, a % b)
    else:
        return a


def wyniki1():
    a = int(input('Podaj a: '))
    b = int(input('Podaj b: '))
    print(f'NWD z RWND: {RNWD(a,b)}')
    print(f'NWD z ENWD: {ENWD(a, b)}')

def zmierz_czas(func, *args, **kwargs):
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time

def wyniki2():
    n = int(input('Podaj n: '))
    m = int(input('Podaj m: '))
    czasy_rnwd = []
    czasy_enwd = []
    for q in range(1, m):
        czasy_rnwd.append(zmierz_czas(RNWD, n, q))
        czasy_enwd.append(zmierz_czas(ENWD, n, q))

    fig, ax = plt.subplots(figsize=(10,8))
    ax.plot(czasy_rnwd, label='RNWD')
    ax.plot(czasy_enwd, label='ENWD')
    plt.ylabel('Czas')
    plt.legend()
    plt.show()

