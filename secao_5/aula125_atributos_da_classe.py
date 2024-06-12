class Pessoa:
    ANO_ATUAL = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ANO_ATUAL - self.idade
    
p1 = Pessoa('X', 12)
print(p1.ANO_ATUAL)
print(p1.get_ano_nascimento())