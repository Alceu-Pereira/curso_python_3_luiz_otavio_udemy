produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dict_comprehesion = {
    chave.upper(): valor
    if isinstance(valor, str)
    else valor
    for chave, valor in produto.items()
    if isinstance(valor, (int, float)) and valor > 2
}

print(dict_comprehesion)

set_comprehension = {i for i in range(10)}
print(set_comprehension)