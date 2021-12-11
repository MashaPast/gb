import sys


def add(num):
    with open('bakery.cvs', 'a', encoding='utf-8') as f:
        f.write('\n' + str(num[1]))


add(sys.argv)
