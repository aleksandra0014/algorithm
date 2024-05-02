from robots_stack import Robot

class RobotyKolejka:
    def __init__(self):
        self.kolejka = []

    def dodaj(self):
        robot = Robot()
        robot = robot.tworz_robota()
        self.kolejka.append(robot)

    def dodaj_kilka(self, n):
        for i in range(n):
            self.dodaj()

    def usun(self):
        if len(self.kolejka) == 0:
            return None
        else:
            usuniety = self.kolejka.pop(0)
            return print(f' Usunięty robot: {usuniety}')

    def usun_wszytkich(self):
        while len(self.kolejka) > 0:
            self.kolejka.usun()

    def pokaz(self):
        print('Kolejka robotów:')
        for i in self.kolejka:
            print(i)

if __name__ == '__main__':
    kolejka_robot = RobotyKolejka()
    kolejka_robot.dodaj_kilka(2)
    kolejka_robot.pokaz()
    kolejka_robot.usun()