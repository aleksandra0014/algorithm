import random
import string

import pandas as pd
from robots_stack import Robot


class Node:
    def __init__(self):
        self.robot = Robot()
        self.robot.tworz_robota()
        self.data = [self.robot.typ, self.robot.zasieg, self.robot.cena, self.robot.kamera]
        self.id = input('Podaj id: ')
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def dodaj_robot(self):
        new_node = Node()
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def usun_robot(self, id):
        current = self.head
        if current is None:
            print('Lista jest pusta')
            return None
        if current.id == id:
            print(f'Usunięto robota {current.id, current.data}')
            self.head = current.next
            return
        while current.next:
            if current.next.id == id:
                print(f'Usunięto robota {current.id, current.data}')
                current.next = current.next.next
                return
            current = current.next
        return 'Nie znaleziono robota do usunięcia.'

    def znajdz_robota(self, id):
        current = self.head
        while current:
            if current.id == id:
                print(f'Znaleziono robota {current.id, current.data}')
                return
            current = current.next
        return 'Nie znaleziono robota'

    def pokaz(self):
        current = self.head
        while current:
            print(current.id, current.data)
            current = current.next


class LinkedListTabela:
    def __init__(self):
        self.tablica = pd.DataFrame(columns=['Indeks', 'Id', 'Typ', 'Cena', 'Zasięg', 'Kamera', 'Następny', 'Istnieje'])

    def random_id(self):
        sth = string.ascii_letters + string.digits
        return ''.join(random.choice(sth) for _ in range(4))
    def dodaj_robota(self):
        robot = Robot()
        robot.tworz_robota()
        id = input('Podaj id robota: ')
        indeks = len(self.tablica)
        if indeks > 0:
            self.tablica.loc[indeks - 1, 'Następny'] = indeks
        self.tablica.loc[indeks] = [indeks, id, robot.typ, robot.cena, robot.zasieg, robot.kamera, None, True]
        print("Dodano robota do listy.")
        print(self.tablica)

    def usun_robota(self, id):
        znaleziony = False
        for i in range(len(self.tablica)):
            if self.tablica.at[i, 'Id'] == id:
                znaleziony = True
                indeks = self.tablica.at[i, 'Indeks']
                if indeks == 0:
                    self.tablica = self.tablica.iloc[1:]
                elif indeks == len(self.tablica)-1:
                    self.tablica.at[indeks, 'Istnieje'] = False
                else:
                    self.tablica.at[indeks, 'Istnieje'] = False
                    pop_indeks = self.tablica.at[indeks, 'Indeks'] - 1
                    pop_nastepny = self.tablica.at[indeks, 'Następny']
                    self.tablica.at[indeks, 'Następny'] = None
                    self.tablica.at[pop_indeks, 'Następny'] = pop_nastepny
                print("Usunięto robota z listy.")
                print(self.tablica)
        if not znaleziony:
            print('Nie znaleziono robota.')


    def wyszukaj_robota(self, id):
        znaleziony = False
        for i in range(len(self.tablica)):
            if self.tablica.at[i, 'Id'] == id:
                znaleziony = True
                indeks = self.tablica.at[i, 'Indeks']

                if indeks >= len(self.tablica):
                    print("Podany indeks nie znajduje się na liście.")
                    return
                robot = self.tablica.loc[indeks]
                print("Znaleziono robota.")
                print(robot)
        if not znaleziony:
            print('Nie znaleziono robota.')

    def dodaj_z_pliku(self, nazwa):
        df = pd.read_csv(nazwa)
        for i in range(len(df)):
            typ, cena, zasieg, kamera = df.iloc[i].values
            indeks = len(self.tablica)
            if indeks > 0:
                self.tablica.loc[indeks - 1, 'Następny'] = indeks
            id = self.random_id()
            self.tablica.loc[indeks] = [indeks, id, typ, cena, zasieg, kamera, None, True]
        print(self.tablica)


def wersja1():
    l = LinkedList()
    n = int(input('Ile robotów dodać? '))
    for i in range(n):
        l.dodaj_robot()

    print('1')
    l.pokaz()
    l.usun_robot('1')
    print('2')
    l.pokaz()
    l.znajdz_robota('2')

def wersja2():
    lt = LinkedListTabela()
    lt.dodaj_z_pliku('plik_roboty2.csv')
    lt.dodaj_robota()
    lt.wyszukaj_robota('9sd3')
    lt.usun_robota('9sd3')



if __name__ == '__main__':
    wersja2()