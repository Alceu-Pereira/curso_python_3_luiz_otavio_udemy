lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Alceu'}]

for item in lista:
    if isinstance(item, str):
        print('STR', item.upper())
    else:
        print(item)
   