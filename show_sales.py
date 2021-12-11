import sys


def show(num):
    with open('bakery.cvs', 'r', encoding='utf-8') as f:
        paragraphs = f.readlines()
        counter = 0
        for line in paragraphs:
            counter += 1
            try:
                if int(num[1]) <= counter <= int(num[2]):
                    print(line)
            except IndexError:
                if int(num[1]) == counter:
                    print(line)


show(sys.argv)
