import random
import pandas as pd

class Roboty:
    def __init__(self):
        self.par_typ = {'AGV', 'AFV', 'ASV', 'AUV'}
        self.par_cena_start = 0
        self.par_cena_end = 10000
        self.par_zasieg = list(range(0, 100))
        self.par_kamera = {0, 1}
        self.lista_robot = []

    def generuj(self, N):
        for i in range(N):
            typ = random.choice(list(self.par_typ))
            cena = random.uniform(self.par_cena_start, self.par_cena_end)
            zasieg = random.choice(self.par_zasieg)
            kamera = random.choice(list(self.par_kamera))
            robot = (typ, cena, zasieg, kamera)
            self.lista_robot.append(robot)
        return self.lista_robot

    def wyswietl_zapisz(self, nazwa_sciezki):
        df = pd.DataFrame(self.lista_robot, columns=['typ', 'cena', 'zasieg', 'kamera'])
        print(df)
        df.to_csv(f'{nazwa_sciezki}', index=False)
        print('Zapisano listę robotów do pliku.')

    def odczytaj_wyswietl(self, nazwa_sciezki):
        df = pd.read_csv(f'{nazwa_sciezki}')
        print(df)


roboty = Roboty()
roboty.generuj(5)
roboty.wyswietl_zapisz('plik_roboty2')

