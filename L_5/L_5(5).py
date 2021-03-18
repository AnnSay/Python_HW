''' Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран'''

"""from random import randint"""
"""with open("text_5", 'w', encoding='utf-8') as my_file:
    my_list = [randint(1,100) for _ in range(100)]
    my_file.write(''.join((map(str, my_list))))

print((f'Сумма элементов - {sum(my_list)}'))"""

from random import randint

with open("text_5.txt", mode='w+', encoding='utf-8') as my_file:
    my_file.write(''.join([str(randint(1, 1000)) for _ in range(100000)]))
    my_file.seek(0)
    print(sum(map(int, my_file.readline().split())))
