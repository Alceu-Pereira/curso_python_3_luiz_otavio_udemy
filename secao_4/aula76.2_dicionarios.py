pessoa = {
    'nome': 'Alceu',
    'sobrenome': 'Pereira',
    }

pessoa.setdefault('idade', 24)
print(pessoa['idade'])
print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))