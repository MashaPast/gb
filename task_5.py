"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
"""


def val_checker(verbosity):
    def _val_checker(fun):
        def wrapper(x):
            if verbosity(x) is False:
                raise ValueError('Значение отрицательное')
            else:
                return fun(x)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
