# Импортируем нужные библиотеки
import threading
import time
from queue import Queue
import random


# Создадим классы
class Cafe:
    # Пустой список потоков
    threads = []

    # инициация параметров
    def __init__(self, *tables) -> None:
        self.tables = list(tables)
        self.q = Queue()

    # Рассадим гостей за столы
    def guest_arrival(self, *guests):
        guests = list(guests)
        # пробежим по списку столов
        for i in range(len(self.tables)):
            # займем стол
            self.tables[i].guest = guests[i]
            # поток
            th = guests[i]
            # добавим поток в список потоков
            self.threads.append(th)
            # Стартуем поток
            th.start()
            # Сообщим о посадке
            print(f'{guests[i].name} сел(-а) за стол номер {self.tables[i].number}')
        # Если посетителей больше
        if len(guests) > len(self.tables):
            # Поставим осиавшихся гостей в очередь
            for j in range(len(self.tables), len(guests)):
                self.q.put(guests[j])
                # Сообщим что гость в очереди
                print(f'{guests[j]} в очереди')

    # Функция обслуживания
    def discuss_guests(self):
        # До тех пор пока очередь НЕ пуста или за столом кто то сидит
        while not self.q.empty() or any(table.guest for table in self.tables):
            # Пробежим по столам списка столов
            for table in self.tables:
                # Если стол занят но поток завершен (гость покушал)
                if not table.guest is None and not table.guest.is_alive():
                    # Известим что гость покушал
                    print(f'{table.guest} покушал(-а) и ушел(ушла).')
                    # Освободим стол
                    print(f'Стол {table.number} свободен')
                    table.guest = None
                # Если очередь не пуста и есть свободный стол
                if not self.q.empty() and table.guest is None:
                    # Возмем гостя из очереди и усадим за стол
                    table.guest = self.q.get()
                    print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    # Сформируем поток
                    th = table.guest
                    # Стартанем поток
                    th.start()
                    # Добавим поток в список
                    self.threads.append(th)
                # Класс столов


class Table:
    def __init__(self, number):
        self.number = number
        self.quest = None


# Класс потоков
class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(1, 6))

    def __str__(self):
        return self.name


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()