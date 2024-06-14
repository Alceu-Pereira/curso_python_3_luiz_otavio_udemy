import copy

pessoa = {
    'nome': 'Alceu',
    'sobrenome': 'Pereira',
    'idade': 24,
    'endereços': ['Rua X', 'Numero 321']
    }

pessoa2 = copy.deepcopy(pessoa)

pessoa2['endereços'][0] = 'Rua W'
pessoa2['nome'] = 'Outro'

print(pessoa)
print(pessoa2)