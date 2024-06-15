class Pessoa:
    ano = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hi')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anonima', idade)

p1 = Pessoa('Alceu', 24)
p2 = Pessoa.criar_com_50_anos('Alceu')
p3 = Pessoa.criar_anonimo(30)

print(p3.nome, p3.idade)