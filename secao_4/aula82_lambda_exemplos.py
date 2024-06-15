def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return multiplicador * numero
    return multiplica

print(
    executa(
        lambda x, y: x + y, 2, 6
    )
)

print((executa(
    lambda multiplicador: lambda numero: multiplicador * numero, 2
))(2))

print(
    executa(
        lambda *args: sum(args), 2, 3, 4
    )
)