# print(list(range(10)))

# lista = []
# for i in range(10):
#     lista.append(i)
# print(lista)

# lista = [
#     i ** 2
#     for i in range(10)
# ]
# print(lista)

produtos = [
    {'nome': 'Produto 1', 'preco': 20, },
    {'nome': 'Produto 2', 'preco': 10, },
    {'nome': 'Produto 3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] == 10 
    else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')