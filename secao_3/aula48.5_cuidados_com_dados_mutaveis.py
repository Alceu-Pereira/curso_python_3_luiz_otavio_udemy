lista_a = ['A', 'B', []]
lista_b = lista_a
lista_c = lista_a.copy()
lista_c[0] = 'D'

lista_b[0] = 'C'
print(lista_a)
print(lista_c)
