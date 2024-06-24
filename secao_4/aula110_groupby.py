from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
]

ordenado = sorted(alunos, key=lambda dic: dic['nota'])

grupos = groupby(ordenado, key=lambda dic: dic['nota'])

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)