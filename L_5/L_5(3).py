"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""
"""with open('text_2.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя ведичина дохода сотрудников = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
           f'Фамилии работников чья зп меньше 20000 {[e[0] for  e in employees_dict.items() if e[1] < 20000]}')"""


def text_2():
    wages = {}
    try:
        with open('text_2.txt', 'r', encoding='utf-8') as file:
            for line in file:
                wages[line.split()[0]] = float(line.split()[1])
        print('Фамилии работников чья зп меньше 20000: ')
        for name, wage in wages.items():
            if wage < 20000:
               print(name)
        print(f'Средняя зарплата равна {sum(wages.values()) / len(wages)}')
    except IOError:
        print('IOError')
    except:
        print('Другая ошибка')
