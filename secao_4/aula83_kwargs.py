pessoa = {
    'nome': 'Alceu',
    'sobrenome': 'Pereira',
}

dados_pessoa = {
    'idade': 24,
    'altura': 1.64,
}

pessoa_completa = {**pessoa, **dados_pessoa, 'idade': 23}

print(pessoa_completa)

def kwargs_(**kwargs):
    print({**kwargs})

kwargs_(nome='Alceu', sobrenome='Pereira')