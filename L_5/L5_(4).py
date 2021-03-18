"""Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

"""rus_dic = {'One': 'Один', 'Two': 'Два', 'Tree': 'Три', 'Four': 'Четыре'}

with open("text_44", 'w', encoding='utf-8') as new_file:
    with open("text_4", encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])"""



from googletrans import Translator

with open("text_44.txt", 'w', encoding='utf-8') as f:
    with open("text_4.txt", 'r', encoding='utf-8') as f1:
        text = f1.read()
    try:
        f.write(Translator().translate(text, dest='ru').text)
    except AttributeError:
        print('Attribute Error')



