lista = [1, 2, 3, 4]
indice_2 = lista[2] 
lista[2] = 9
del lista[2]
lista.pop()
lista.pop()
lista.append(30)
ultimo_valor = lista.pop(-1)
lista.append(90)


print(lista)
print(indice_2)
print(ultimo_valor)