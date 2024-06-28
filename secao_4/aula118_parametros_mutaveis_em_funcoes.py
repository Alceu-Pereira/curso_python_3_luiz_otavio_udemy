def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

# lista1 = []

cliente1 = adiciona_clientes('Alceu')
adiciona_clientes('Ritielly', cliente1)
print(cliente1)

# lista2 = []
cliente2 = adiciona_clientes('Alceu')
adiciona_clientes('Ritielly', cliente2)
print(cliente2)