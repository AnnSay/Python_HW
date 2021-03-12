"""Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов"""


def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'Вводить можно только числа'


print(my_func(int(input('введите первый номер: ')), int(input('введите второй номер: ')),
              int(input('введите третий номер: '))))
