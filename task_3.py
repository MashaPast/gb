"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--authapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django.

"""

import os
from shutil import copy

dir_path = 'my_project/templates'
for subdir, dirs, files in os.walk('my_project'):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".html"):
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            copy(filepath, dir_path)
            print(filepath)



