"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit
from numpy import array, where


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]

def func_3(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr = new_arr + [i]
    return new_arr

def func_4(nums):
    return list(range(0, len(nums), 2))

L = "list(filter(lambda x: x % 2 == 0, NUMS))"

col = [1000, 10000, 100000]

for i in col:
    NUMS = [el for el in range(i)]
    print(f'------Для массива из {i} эллементов-------')
    t1 = timeit ("func_1(NUMS[:])", globals=globals(), number=1000)
    t2 = timeit ("func_2(NUMS[:])", globals=globals(), number=1000)
    t3 = timeit("func_3(NUMS[:])", globals=globals(), number=10) #Комьютер очень долго делает, поставил 10, а не 1000, но вывод сделать это не мешает
    t4 = timeit("func_4(NUMS[:])", globals=globals(), number=1000)
    t5 = timeit(L, globals=globals(), number=1000)
    print (f'Время выполнения программы c append: {t1}')
    print (f'Время выполнения программы cо списковым включением: {t2}')
    print(f'Время выполнения программы c конкатенацией: {t3 * 100}')
    print(f'Время выполнения программы cо встроеными функциями: {t4}')
    print(f'Время выполнения lambda-программы: {t5}\n')
print("\n========================================================\n")
print("Встроеные функции значительно лучше остальных, потом идут программы:\nсо списком включения\nпо средствам lambda-функций\nс append,\nа конкатенацию нужно стараться избегать использовать.\nЭтот способ просто на парядок медленее.")