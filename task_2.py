sentence_list = []
new_list = []
"""
с плюсом разобраться
"""
for el in sentence_list:
    if type(el) is int:
        new_list.append('"')
        if len(el) == 1:
            el = "0" + el
        new_list.append(el)
        new_list.append('"')
    else:
        new_list.append(el)



