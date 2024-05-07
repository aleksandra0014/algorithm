from linear_search import create_list


class Robot:
    def __init__(self, key, param):
        self.key = key
        self.param = param


class LinkedList:
    def __init__(self, robot):
        self.robot = robot
        self.next = None


class HashTable:
    def __init__(self, size, load_factor):
        self.size = size
        self.table = [None] * size
        self.load_factor = load_factor
        self.count = 0

    def hash(self, key):
        return key % self.size

    def insert(self, robot):
        index = self.hash(robot.key)
        if self.table[index] is None:
            self.table[index] = LinkedList(robot)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = LinkedList(robot)
            self.count += 1
            if self.count / self.size > self.load_factor:
                self.rehash()

    def rehash(self):
        new_size = self.size * 2
        new_table = [None] * new_size
        for i in range(self.size):
            current = self.table[i]
            while current is not None:
                next_node = current.next
                index = current.robot.key % new_size
                current.next = new_table[index]
                new_table[index] = current
                current = next_node
        self.size = new_size
        self.table = new_table

    def search(self, key):
        index = self.hash(key)
        current = self.table[index]
        while current is not None:
            if current.robot.key == key:
                return current.robot.param
            current = current.next
        return "brak"


def generate_key(arr):
    total = 0
    for i in arr:
        if isinstance(i, str):
            for char in i:
                total += ord(char)
        elif isinstance(i, (int, float)):
            total += int(i)
    return total


def generate_robot(arr):
    key = generate_key(arr)
    param = arr
    robot = Robot(key, param)
    return robot


if __name__ == '__main__':
    arr = create_list('plik_roboty2.csv')
    alpha = float(input('Podaj współczynnik wypełnienia tablicy: '))
    size = len(arr)
    hash_tab = HashTable(size, alpha)
    for i in arr:
        print(i)
        r = generate_robot(i)
        # print(r.key) # 6495 7113 252 9943 3446
        hash_tab.insert(r)
    print(hash_tab.table)
    print('Wyszukaj po kluczu: 9943')
    print(hash_tab.search(9943))
