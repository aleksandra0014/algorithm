import random

def eucklides(a, b):
    if b:
        return eucklides(b, a % b)
    else:
        return a


def rozszerzony_eucklides(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = rozszerzony_eucklides(b, a % b)
    return d, y, x - (a//b)*y


def odwr_mult(a, m):
    d, x, y = rozszerzony_eucklides(a, m)
    if d != 1:
        raise ValueError("Nie istnieje muliplikatywna odwrotność")
    return x % m


def spr_czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierwsza = int(n ** 0.5) + 1
    for dzielnik in range(3, pierwsza, 2):
        if n % dzielnik == 0:
            return False
    return True


def generuj_klucze(p, q):
    if not (spr_czy_pierwsza(p) and spr_czy_pierwsza(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    pq = p * q
    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)

    # USprawdzenie czy e i phi są względnie pierwsze
    g = eucklides(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = eucklides(e, phi)

    d = odwr_mult(e, phi)

    return ((e, pq), (d, pq))


def koduj(pk, plaintext):
    key, n = pk
    # Funkcja pow() oblicza potęgę liczby x podniesionej do potęgi y modulo z
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher


def dekoduj(pk, ciphertext):
    key, n = pk
    aux = [str(pow(char, key, n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)


def rsa_program():
    p = int(input("Podaj liczbę pierwszą: "))
    q = int(input("Podaj kolejną liczbę pierwszą, inną od poprzedniej: "))
    print("Tworzenie kluczy ... ")
    public, private = generuj_klucze(p, q)
    print("Klucz publiczny", public, "oraz klucz prywatny", private)
    print("--" * 100)
    message = input("Podaj wiadomość do zaszyfrowania: ")
    zakodowana_msg = koduj(public, message)
    print("Zakodowana wiadomość: ", ''.join(map(lambda x: str(x), zakodowana_msg)))
    print("Odkodowywanie kluczem prywatnym, ... ", private, " . . .")
    print("Odszyfrowana wiadomość: ", dekoduj(private, zakodowana_msg))

rsa_program()