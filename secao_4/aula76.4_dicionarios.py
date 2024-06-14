pessoa = {
    'nome': 'Alceu',
    'sobrenome': 'Pereira',
}

# print(pessoa.get('idade'))
# nome = pessoa.pop('nome')
# print(nome)

# ultima_chave = pessoa.popitem()
# print(ultima_chave)

pessoa.update({
    'nome': 'Outro',
    'idade': 24,
})

print(pessoa)