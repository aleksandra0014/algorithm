class Robot:
    def __init__(self):
        self.typ = None
        self.cena = None
        self.zasieg = None
        self.kamera = None

    def tworz_robota(self):
        typ = input("Podaj typ (do wyboru: AGV, AFV, ASV, AUV):")
        if typ not in ['AGV', 'AFV', 'ASV', 'AUV']:
            raise ValueError("Zła wartość typu.")
        try:
            cena = float(input("Podaj cene (przedział od 0 do 10000): "))
        except ValueError:
            print("Zła wartość ceny.")
        try:
            zasieg = int(input("Podaj zasieg (przedział od 0 do 100 - liczby całkowite): "))
        except ValueError:
            print("Zła wartość zasięgu.")
        kamera = int(input('Czy robot ma mieć kamerę (0 - nie, 1 - tak): '))
        if kamera != 0 and kamera != 1:
            raise ValueError("Zła wartość.")
        self.typ = typ
        self.cena = cena
        self.zasieg = zasieg
        self.kamera = kamera
        return (self.typ, self.cena, self.zasieg, self.kamera)


class StosRoboty:
    def __init__(self):
        self.stack = []

    def push(self):  # dodawanie
        robot = Robot()
        robot = robot.tworz_robota()
        self.stack.append(robot)

    def push_more(self, n):
        for i in range(n):
            self.push()


    def pop(self):  # usuwanie
        poped = self.stack.pop(len(self.stack) - 1)
        return print(f' Usunięty robot: {poped}')


    def pop_all(self):
        while len(self.stack) > 0:
            self.stack.pop()

    def show_stack(self):
        print('Stos robotów:')
        for i in self.stack:
            print(i)

if __name__ == '__main__':
    stos = StosRoboty()
    stos.push_more(2)
    stos.show_stack()
    stos.pop()