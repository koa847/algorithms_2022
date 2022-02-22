"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))

enter_num = 1234567890

for i in (1, 2 , 3, 4):
    s = f'revers_{i}'
    st = f'{s}(enter_num)'
    t = timeit (st, globals=globals(), number=1000)
    print(f'Время выполнения программы {s} составляет {t} секунд')
print('\n\n')
"""
Срез и реверс очень быстрые программы, причем срез немного даже быстрее реверса, хотя реверс использует исключительно встроеные функции,
рекурсия и цикл немного проигрывают, поэтому для данной задачи лучше использовать срез, ну или реверс, как наиболее компактный и совсем незначительно проигрывающий срезу
"""

run("for i in range(1000): revers_1(enter_num)")
run("for i in range(1000): revers_2(enter_num)")
run("for i in range(1000): revers_3(enter_num)")
run("for i in range(1000): revers_4(enter_num)")