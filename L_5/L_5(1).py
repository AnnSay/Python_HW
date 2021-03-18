"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строк"""

"""with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введит данные для записи в файл \nдля окончания ввода введите пустую строку: ')
        if not line:
            break
        print(line, file=f)"""

"""my_file = open('text_1.txt', 'w', encoding='utf-8')
line = ' '
while line:
    line = input('Введите текст или нажмите Enter для завершения программы: ')
    my_file.write(f'{line}\n') if line != ' ' else my_file.close()"""

print('Введите текст или нажмите Enter для завершения программы: ')
with open('text_1.txt', 'w', encoding='utf-8') as my_file:
    while (line := input()) != '':
        my_file.write(f'{line}\n')
