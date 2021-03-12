"""Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""


def int_func():
    for word in input('Введите тест маленькими латинскими буквами: \n').split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f'{word} - Введите тест маленькими латинскими буквами')


int_func()
