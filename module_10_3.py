# Загрузим необходимые библиотеки
import threading
import time
from random import randint
# Объявим блокировку
lock = threading.Lock()

# Создадим класс
class Bank:
  def __init__(self):
    self.balance = 0
  # Процедура пополнения баланса
  def deposid(self):
    for __ in range(100):
      rand_many = randint(50, 500)
      self.balance = self.balance + rand_many
      print(f'Пополнение {rand_many}. Баланс: {self.balance}')
      # Снятие блокировки
      if self.balance >= 500 and lock.locked():
        print(f'Счет разблокирован для снятия. Баланс: {self.balance}')
        lock.release()
      time.sleep(0.001)
  # Процедура снятия
  def take(self):
    for __ in range(100):
      take_many = randint(50, 500)
      print(f'Запрос на {take_many}')
      # Если денег хватит снимаем
      if take_many <= self.balance:
        self.balance = self.balance - take_many
        print(f'Снятие {take_many}. Баланс: {self.balance}')
      # Если не хватает то счет блокируем
      else:
        lock.acquire()
        print('Операция заблокирована не достаточно средств')
      time.sleep(0.001)

# Создаем экземпляр банка
bk = Bank()
# Создаем потоки
thread_1 = threading.Thread(target=Bank.deposid, args=(bk, ))
thread_2 = threading.Thread(target=Bank.take, args=(bk, ))
# Стартуем потоки
thread_1.start()
thread_2.start()