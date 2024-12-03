# Загрузим необходимые библиотеки
import datetime
import os
import multiprocessing

# Сформируем список файлов
list_files = [file for file in os.listdir() if file.endswith('.txt')]

# Объявим функцию
def read_info(name):
    # файл хранения чтения файлов построчно
    all_data = []
    # Откроем файл для чтения
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            # Прочитаем
            line = file.readline()
            for line in file:
                # положим строку в итоговый файл
                all_data.append(line)
            # Если строка пустая прекращаем
            if line == '':
                break


if __name__ == '__main__':
    # Замер времени линейного чтения
    start_l = datetime.datetime.now()

    for files in list_files:
        read_info(files)

    end_l = datetime.datetime.now()
    print(f'Время затраченое линейным способом {end_l - start_l}')
    # Замер времени мультипроцессорного чтения
    start_m = datetime.datetime.now()

    # Запустим мультипроцессорное чтение
    # Наиболее оптимольное значение процессоров равно 5
    # Все остальные значения процессоров показывают худшие результаты
    with multiprocessing.Pool(processes=5) as pool:
        result = pool.map(read_info, list_files)

    end_m = datetime.datetime.now()
    print(f'Время затраченое мультипроцессорным способом {end_m - start_m}')

