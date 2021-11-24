import math
"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: 
до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * 
в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:

duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек

"""

number = int(input("Enter seconds: "))

if number < 60:
    print(str(number) + " сек" )
elif 3660 > number >= 60:
    print(str(math.floor(number/60)) + " мин " + str(number % 60) + " сек")

elif 86400 > number >= 3600:
    hours = math.floor(number / 3600)
    res_sec = (number - (hours * 3600))
    mins = math.floor(res_sec/60)
    sec = res_sec - (mins * 60)
    print(str(math.floor(hours)) + " час " + str(mins) + " мин " + str(sec) + " сек")

elif number >= 86400:
    days = math.floor(number / 86400)
    hours = math.floor(number / 3600) - days * 24
    print(hours)
    mins = math.floor(math.floor(number - days * 86400 - hours * 3600)/60)
    sec = math.floor(math.floor(number - days * 86400 - hours * 3600 - mins * 60))
    print(str(days) + " дней " + str(hours) + " час " + str(mins) + " мин " + str(sec) + " сек")
