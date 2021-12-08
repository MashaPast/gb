"""
3. Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)

### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект.

Подсказка: использовать возможности python, изученные на уроке.
"""

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б'
]


def create_cort(tuts, kls):
    for t, k in zip(tuts, kls):
        if len(tutors) > len(klasses):
            while len(tutors) != len(klasses):
                klasses.append(None)
        result = (t,) + (k,)
        yield result


res = create_cort(tutors, klasses)
print(type(res))

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

# print(next(res))
