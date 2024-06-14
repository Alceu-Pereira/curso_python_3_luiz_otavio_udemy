pessoa = {
    'nome': 'Alceu',
    'sobrenome': 'Pereira',
    'idade': 24,
    'altura': 1.64,
    'endereços': 
    [
        {'rua': 'xxx', 'numero': 1},
        {'rua': 'yyy', 'numero': 2},
    ],
}

print(pessoa['nome'])

pessoa['nome'] = 'Outro nome'

del pessoa['sobrenome']
print(pessoa['nome'])
print(pessoa)

print(pessoa.get('sobrenome'))