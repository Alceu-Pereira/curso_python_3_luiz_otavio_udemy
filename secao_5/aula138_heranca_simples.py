class Pessoa:
    cpf = '123.456.789-10'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_cls(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    cpf = '987.654.321-01'


c1 = Cliente('Alceu', 'Pereira')
c1.falar_nome_cls()
a1 = Aluno('X', 'Y')
a1.falar_nome_cls()
print(a1.cpf)
# help(Cliente)