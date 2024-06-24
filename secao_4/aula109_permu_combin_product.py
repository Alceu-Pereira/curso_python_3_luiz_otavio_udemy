from itertools import combinations, permutations, product

def meu_print(iterator):
    print(*list(iterator), sep='\n')

pessoa = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['listrada', 'lisa'],
    ['mas', 'fem'],
]

# combinacao = combinations(pessoa, 2)
# lista = list(combinacao)
# meu_print(lista)

# permutacao = permutations(pessoa, 2)
# meu_print(permutacao)

meu_print(product(*camisetas))
