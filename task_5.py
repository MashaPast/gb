import random


"""
Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
(например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
(должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать,
что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""

prices = []

for i in range(0, 10):
    prices.append(random.randint(30, 150))
    prices.append(round(random.uniform(30, 150), 2))

print("Объект списка после сортировки остался тот же")
print(hex(id(prices)))
prices.sort()
print(hex(id(prices)))




def modify_list(prices):
    new_prices = []
    for el in prices:
        if type(el) is float:
            cop = str(round(el - int(el), 2))[2:]
            if cop == '0':
                cop = '00'
            new_prices.append(str(int(el)) + ' руб ' + cop + ' коп')
        else:
            new_prices.append(str(int(el)) + ' руб')

    return new_prices


new_str = ', '.join(modify_list(prices))
print(f"Список цен через запятую {new_str}")


reversed_prices = sorted(prices, reverse=True)
reversed_prices_rubs = modify_list(reversed_prices)
print(f"Список отсортированный по убыванию: {reversed_prices_rubs}")
print(f"Самые дорогие товары: {reversed_prices_rubs[:5]}")
