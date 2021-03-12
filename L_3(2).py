"""Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой.
"""


def personal_info(**kwargs):
    return ' '.join(kwargs.values())


print(personal_info(name=input('Введите Ваше имя: '), surname=input('Введите Вашу фамилию: '),
                    birthday=input('Введите дату Вашего рождения : '), city=input('Введите Ваш город проживания: '),
                    email=input('Введите Ваш email : '), phone_number=input('Введите Ваш номер телефона: ')))