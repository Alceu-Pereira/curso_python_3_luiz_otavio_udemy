class Pessoa:
    ANO_ATUAL = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ANO_ATUAL - self.idade

dados = {'nome': 'X', 'idade': 12}
p1 = Pessoa(**dados)
p1.__dict__['outra'] = 'coisa'
print(p1.__dict__)
print(vars(p1))