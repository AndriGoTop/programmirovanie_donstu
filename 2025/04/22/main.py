import sys
import gc
import os
import psutil

# # создаем объект
# a = [1, 2, 3]

# # Проверка счетчика ссылок
# print(sys.getrefcount(a))  # 2 ссылки, т.к. первая ссылка когда проходит присваивание, вторая для как аргумент функции

# b = a
# print(sys.getrefcount(a))
# print(sys.getrefcount(b))

# # Удаляем связь
# del a
# print(sys.getrefcount(b))

# ------------------------------------------

# # создаем объект

# a = {}
# b = {}
# a['b'] = b
# b['a'] = a  # создается циклическая ссылка (a ссылает на b, а b ссылается на a)

# print(gc.get_count())  # выводим сколько переменных, ссылок, связейв в каждом покалении

# del a
# del b  # удалим переменные но ссылки останутся

# gc.collect()  # удалим цикл. списки
# print(gc.get_count())
# gc.enable()  # отключить автоматический сбор мусора

# -------------------------------------------

# функция для получения текущего пользования памяти процессора
def get_memory_usage():
    proccess=psutil.Process(os.getpid())
    return proccess.memory_info().rss/(1024*1024)

large_list = [i for i in range(1000000)]

# проверяем кол-ва объектов, отслеживаемых сборщиком
print('кол-во до сборки:', gc.get_count())

# Проверяем использование памяти до сборки
memory_before = get_memory_usage() 
print(f'Использование памяти до сборки: {memory_before:.2f} MB')

del large_list

# Запускаем принудительно сборщик
print('кол-во после сборки:', gc.get_count())

memory_after = get_memory_usage()
print(f'Использование памяти после сборки: {memory_after:.2f} MB')

# Вычисляем освобожденную память
feed_memory = memory_before - memory_after 
print(f'Использование памяти до сборки: {feed_memory:.2f} MB')
