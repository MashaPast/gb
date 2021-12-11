"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

import itertools

result = {}

hobbies = open('hobby.csv', 'r', encoding='utf-8')
users = open('users.csv', 'r', encoding='utf-8')


for el_h, el_u in itertools.zip_longest(hobbies, users, fillvalue=None):
    try:
        el_u = el_u.replace('\n', '')
        if el_h is not None:
            result[el_u.replace(',', ' ')] = el_h.replace('\n', '')
        else:
            result[el_u.replace(',', ' ')] = el_h
        with open('task2.txt', 'w') as file:
            file.write(str(result))
    except AttributeError:
        print(result)
        exit(1)

print(result)
hobbies.close()
users.close()
