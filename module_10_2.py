# Импортируем нужные нам библиотеки
import threading
import time

# Создадим класс управления потоками
class Knight(threading.Thread):
    # инициируем класс-поток
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        # Счетчик дней
        self.days = 0

    # Функция битвы
    def fight(self, remaining_enemies = 100):
        while remaining_enemies > 0:
            self.days += 1
            remaining_enemies -= self.power
            print(f'{self.name}, сражается {self.days} день(дня).., осталось {remaining_enemies} воинов.')
            time.sleep(1)

    # Функция старта
    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight()
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

# Создадим объекты
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

# Стартанем потоки
first_knight.start()
second_knight .start()

first_knight.join()
second_knight .join()

# Проверим работают ли потоки
if not (first_knight.is_alive()) and not(second_knight.is_alive()):
  print('Все битвы закончены')