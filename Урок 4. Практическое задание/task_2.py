"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение мемоизацией
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!

П.С. задание не такое простое, как кажется
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')

print(f"Время для разворачивания числа {num_100} составило: {timeit('recursive_reverse(num_100)', setup='from __main__ import recursive_reverse, num_100', number=10000)}")
# повторный вызов скорость не меняет
#print(f"Время для разворачивания числа {num_100} составило: {timeit('recursive_reverse(num_100)', setup='from __main__ import recursive_reverse, num_100', number=10000)}")
print(f"Время для разворачивания числа {num_1000} составило: {timeit('recursive_reverse(num_1000)', setup='from __main__ import recursive_reverse, num_1000', number=10000)}")
print(f"Время для разворачивания числа {num_10000} составило: {timeit('recursive_reverse(num_10000)', setup='from __main__ import recursive_reverse, num_10000', number=10000)}")


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'

# Поменял значения, чтобы не брать из памяти компьютера, время не изменилось
"""
num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)
"""
print('\nОптимизированная функция recursive_reverse_mem')

print(f"Время для разворачивания числа {num_100} составило: {timeit('recursive_reverse_mem(num_100)', setup='from __main__ import recursive_reverse_mem, num_100', number=10000)}")
print(f"Время для разворачивания числа {num_1000} составило: {timeit('recursive_reverse_mem(num_1000)', setup='from __main__ import recursive_reverse_mem, num_1000', number=10000)}")
print(f"Время для разворачивания числа {num_10000} составило: {timeit('recursive_reverse_mem(num_10000)', setup='from __main__ import recursive_reverse_mem, num_10000', number=10000)}")

# после мемоизации время выполнения программы не меняется с ростом количества цафр в числе, в отличии от простой рекурсии, а значит имеет место быть, потому что колличество цифр в числе это переменная
# но после мемоизации получилось О(1), что очень хороший результат