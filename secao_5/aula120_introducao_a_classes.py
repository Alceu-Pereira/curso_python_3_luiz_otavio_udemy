# string = 'Alceu'
# print(string.upper())
# print(isinstance(string, str))


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

pessoa_1 = Pessoa('Alceu', 'Pereira')
# pessoa_1.nome = 'Alceu'
# pessoa_1.sobrenome = 'Pereira'


pessoa_2 = Pessoa('Fulano', 'Beltrano')
# pessoa_2.nome = 'Fulano'
# pessoa_2.sobrenome = 'Beltrano'

print(pessoa_1.nome)
print(pessoa_1.sobrenome)
print()
print(pessoa_2.nome)
print(pessoa_2.sobrenome)