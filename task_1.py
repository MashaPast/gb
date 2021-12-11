"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
"""


with open('logs.txt', 'r') as the_file:
    paragraphs = the_file.readlines()
    for el in paragraphs:
        parts = el.split(' ')
        result = (parts[0],) + (parts[5].replace('"', ''),) + (parts[6],)
        with open('task1.txt', 'a') as file:
            file.write(str(result) + ', \n')


