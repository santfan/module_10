# Импортируем нужные библиотеки
from datetime import datetime
from time import sleep, strftime
import threading

# Объявим функцию
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding = 'utf-8') as file:
        for num in range(1, word_count + 1):
            file.write(f'Какое то слово № {num}' + '\n')
            sleep(0.1)
    print(f'Завершена запись в файл {file_name}')

# Начало работы
start_at = datetime.now()
# Вызов функции
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
# Конец работы
end_at = datetime.now()
# Вывод времени работы
func_timer = end_at - start_at
print(f'Функция затратила {func_timer}')

# Теперь сделаем тоже самое но с потоками
# Начало работы с потоками
start_flow = datetime.now()
# Создадим четыре потока
thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
# Стартуем потоки
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
# Приостановим потоки
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
# Конец работы с потоками
end_flow = datetime.now()
# Вывод времени работы потоков
flow_timer = end_flow - start_flow
print(f'Потки затратили {flow_timer}')

# Общий вывод
print(f'Выигрыш времени составил {func_timer - flow_timer}')