# lista = [4, 2, 5, 9, 11, 1, 0, -1]
# lista.sort(reverse=True)

# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda',},
    {'nome': 'Maria', 'sobrenome': 'Oliveira',},
    {'nome': 'Daniel', 'sobrenome': 'Silva',},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira',},
    {'nome': 'Aline', 'sobrenome': 'Souza',},
]

def ordena(item):
    return item['sobrenome']

def exibir(lista):
    for i in lista:
        print(i)
    print()

lista_1 = sorted(lista, key=lambda item: item['nome'])
lista_2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(lista_1)
exibir(lista_2)

